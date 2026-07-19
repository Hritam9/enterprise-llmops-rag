from fastapi import APIRouter

from app.services.rag_service import RAGService

router = APIRouter()


@router.get("/metrics")
async def metrics():

    service = RAGService()

    return service.metrics()
