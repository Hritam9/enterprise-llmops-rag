from fastapi import APIRouter

from app.routes.health import router as health_router
from app.routes.query import router as query_router
from app.routes.upload import router as upload_router
from app.routes.documents import router as document_router
from app.routes.metrics import router as metrics_router

api_router = APIRouter()

api_router.include_router(
    health_router,
    tags=["Health"]
)

api_router.include_router(
    upload_router,
    prefix="/documents",
    tags=["Documents"]
)

api_router.include_router(
    query_router,
    prefix="/chat",
    tags=["Chat"]
)

api_router.include_router(
    document_router,
    prefix="/documents",
    tags=["Documents"]
)

api_router.include_router(
    metrics_router,
    tags=["Monitoring"]
)
