# coding=utf-8
"""Main for aimmocore"""

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

    # 환경을 감지하여 Jupyter 노트북에서 실행 중인지 확인
    def is_jupyter_notebook():
        try:
            shell = get_ipython().__class__.__name__
            if shell == "ZMQInteractiveShell":
                return True  # Jupyter 노트북 또는 Jupyter QtConsole
            elif shell == "TerminalInteractiveShell":
                return False  # IPython 터미널
            else:
                return False  # 기타 환경
        except NameError:
            return False  # IPython이 아님

    # 서버 실행 함수
    def run_server():
        if is_jupyter_notebook():
            # notebook에서 실행시 background에서 실행
            loop = event_loop.get_instance().get_loop()
            loop.run_until_complete(server.serve())
        else:
            # 콘솔에서 실행시 foreground에서 실행
            uvicorn.run(app, host="0.0.0.0", port=viewer_port, log_level="error")

    if is_jupyter_notebook():
        server_thread = threading.Thread(target=run_server, daemon=True)
        server_thread.start()
    else:
        run_server()

    logger.info(f"Curation viewer server started at http://localhost:{viewer_port}/")
    webbrowser.open_new_tab(f"http://localhost:{viewer_port}/")
