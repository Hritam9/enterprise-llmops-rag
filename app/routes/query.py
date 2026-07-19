from fastapi import APIRouter
from fastapi import Depends

from app.dependencies import get_pipeline
from app.schemas.request import QueryRequest
from app.schemas.response import QueryResponse

router = APIRouter()


@router.post(
    "/query",
    response_model=QueryResponse,
)
async def query(

    request: QueryRequest,

    pipeline=Depends(get_pipeline),

):

    result = pipeline.ask(

        request.question

    )

    return QueryResponse(**result)
