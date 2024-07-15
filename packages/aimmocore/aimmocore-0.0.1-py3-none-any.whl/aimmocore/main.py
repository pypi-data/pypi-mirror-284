# coding=utf-8
"""Main for aimmocore"""

import asyncio

import threading
import uvicorn
import webbrowser
from loguru import logger


from IPython import get_ipython
from aimmocore.server.app import app
from aimmocore.core.event import SingletonEventLoop as event_loop


def is_notebook():
    try:
        if "IPKernelApp" in get_ipython().config:  # IPython kernel을 사용하는 경우
            return True
    except Exception:
        pass
    return False


def launch_viewer(viewer_port: int = 10321):
    """Launch dataset viewer

    Args:
        viewer_port (int, optional): Defaults to 10321.
    """
    config = uvicorn.Config(app, host="0.0.0.0", port=viewer_port, log_level="error")
    server = uvicorn.Server(config)

    # 백그라운드에서 실행
    # TODO notebook에서 실행이 아니라면 foreground에서 실행해야함
    def run_server():
        # notebook에서 실행시 background에서 실행
        loop = event_loop.get_instance().get_loop()
        loop.run_until_complete(server.serve())

    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()
    logger.info(f"Curation viewer server started at http://localhost:{viewer_port}/")
    webbrowser.open_new_tab(f"http://localhost:{viewer_port}/")
