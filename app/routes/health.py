from datetime import datetime

from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health():

    return {

        "status": "healthy",

        "timestamp": datetime.utcnow(),

        "application": "Enterprise LLMOps RAG",

        "version": "1.0.0"

    }
