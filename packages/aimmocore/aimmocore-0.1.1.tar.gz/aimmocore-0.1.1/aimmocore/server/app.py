""" Home for AIMMOCore Viewer Server"""

from starlette.applications import Starlette
from starlette.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse
from starlette.routing import Route
from pkg_resources import resource_filename
from aimmocore.server.routers import datasets as asrd


routes = [
    Route("/api/v1/datasets", asrd.DatasetRouter),
    Route("/api/v1/datasets/export", asrd.DatasetExportRouter),
    Route("/api/v1/datasets/files", asrd.DatasetFileRouter),
    Route("/api/v1/datasets/metas/aggregation", asrd.MetaAggregationRouter),
    Route("/api/v1/datasets/embeddings", asrd.EmbeddingRouter),
]


app = Starlette(routes=routes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
static_dir_path = resource_filename("aimmocore", "server/static/")
app.mount("/", StaticFiles(directory=static_dir_path, html=True), name="static")


@app.route("/")
async def viewer(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    return HTMLResponse(open(static_dir_path).read())
