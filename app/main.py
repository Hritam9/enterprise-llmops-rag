from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api import api_router
from app.exception_handlers import register_exception_handlers
from app.middleware import register_middlewares
from monitoring.logger import get_logger

logger = get_logger()


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting Enterprise LLMOps RAG")

    yield

    logger.info("Stopping Enterprise LLMOps RAG")


app = FastAPI(
    title="Enterprise LLMOps RAG",
    version="1.0.0",
    lifespan=lifespan,
)

register_middlewares(app)
register_exception_handlers(app)

app.include_router(api_router)
