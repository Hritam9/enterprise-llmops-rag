from fastapi import FastAPI
from fastapi.responses import JSONResponse

from monitoring.logger import get_logger

logger = get_logger()


def register_exception_handlers(app: FastAPI):

    @app.exception_handler(Exception)
    async def global_exception_handler(
        request,
        exc,
    ):

        logger.exception(exc)

        return JSONResponse(

            status_code=500,

            content={

                "success": False,

                "message": str(exc),
            },
        )
