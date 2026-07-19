import time
import uuid

from fastapi import FastAPI
from starlette.requests import Request

from monitoring.logger import get_logger

logger = get_logger()


def register_middlewares(app: FastAPI):

    @app.middleware("http")
    async def logging_middleware(
        request: Request,
        call_next,
    ):

        request_id = str(uuid.uuid4())

        start = time.time()

        response = await call_next(request)

        duration = round(time.time() - start, 3)

        logger.info(
            f"{request.method} "
            f"{request.url.path} "
            f"{response.status_code} "
            f"{duration}s "
            f"{request_id}"
        )

        response.headers["X-Request-ID"] = request_id

        return response
