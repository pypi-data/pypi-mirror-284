from loguru import logger
from PIL import Image
import aiohttp
from io import BytesIO
import asyncio
from aimmocore.core.database import MongoDB
from pymongo import UpdateOne
from concurrent.futures import ProcessPoolExecutor
from aimmocore import config as conf
from aimmocore.core.event import SingletonEventLoop as sel


def create_thumbnail(image_data, image_id, size=(274, 274)):
    try:
        with Image.open(BytesIO(image_data)) as img:
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            img.thumbnail((max(size), max(size)))
            thumbnail_path = f"{conf.THUMBNAIL_DIR}/{image_id}.jpg"
            img.save(thumbnail_path, "JPEG")
    except Exception as e:  # pylint: disable=broad-except
        logger.error(f"Error creating thumbnail for image ID {image_id}: {e}")


async def download_image(session, image_url):
    """이미지 URL에서 이미지를 다운로드합니다."""
    try:
        async with session.get(image_url) as response:
            response.raise_for_status()
            return await response.read()
    except Exception as e:  # pylint: disable=broad-except
        logger.error(f"Error downloading image {image_url}: {e}")
        return None


async def process_image(document, session, executor):
    """MongoDB 문서에서 이미지 URL을 가져와 썸네일을 생성합니다."""
    image_id = document.get("id")
    image_url = document.get("image_url")
    if image_id and image_url:
        image_data = await download_image(session, image_url)
        if image_data:
            loop = sel.get_instance().get_loop()
            await loop.run_in_executor(executor, create_thumbnail, image_data, image_id)
            return image_id
    return None


async def generate_thumbnail():
    """
    Asynchronously generates thumbnails for images stored in a MongoDB collection.

    This function fetches documents from the MongoDB collection 'raw_files' where the
    'thumbnail' field is neither 'Y' (Yes, completed) nor 'P' (Processing). It updates
    the status of these documents to 'P' to indicate that thumbnail generation is in progress.
    Using a process pool executor, it then processes these images to generate thumbnails.
    Once processing is complete, it updates the document status to 'Y' to mark completion.

    The function uses asyncio for asynchronous operations and a ProcessPoolExecutor for
    CPU-intensive image processing tasks, allowing efficient handling of I/O-bound and
    CPU-bound operations concurrently.

    Prerequisites:
    - A MongoDB instance must be running and accessible.
    - The 'raw_files' collection must exist with the appropriate schema.
    - The function `process_image()` must be defined to handle image processing.

    Uses:
    - aiohttp.ClientSession for managing HTTP sessions.
    - pymongo for MongoDB operations.
    - concurrent.futures.ProcessPoolExecutor for managing a pool of worker processes.

    Raises:
    - pymongo.errors.ConnectionFailure: If the connection to MongoDB fails.
    - Exception: For any unhandled exceptions during the database operations or image processing.

    Returns:
    - None: The function updates the MongoDB documents and logs results; it does not return a value.
    """
    executor = ProcessPoolExecutor(max_workers=2)
    async with aiohttp.ClientSession() as session:
        db = MongoDB()
        db.connect()
        collection = db.engine.raw_files
        documents = await collection.find({"thumbnail": {"$nin": ["Y", "P"]}}, {"_id": 0}).to_list(None)

        image_ids_in_progress = [document.get("id") for document in documents]
        await collection.update_many({"id": {"$in": image_ids_in_progress}}, {"$set": {"thumbnail": "P"}})
        tasks = []
        for document in documents:
            tasks.append(process_image(document, session, executor))
        completed_image_ids = await asyncio.gather(*tasks)

        # Create a list of update requests to set the thumbnail status to "Y" (completed)
        # for successfully processed images.
        requests = [
            UpdateOne({"id": image_id}, {"$set": {"thumbnail": "Y"}})
            for image_id in completed_image_ids
            if image_id is not None
        ]

        # Perform a bulk write operation to update the thumbnail status in MongoDB.
        if requests:
            result = await collection.bulk_write(requests)
            logger.debug(f"Bulk write result: {result.bulk_api_result}")
