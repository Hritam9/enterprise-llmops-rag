from typing import Optional

from pydantic import BaseModel, Field


class QueryRequest(BaseModel):
    """
    Chat request.
    """

    question: str = Field(
        ...,
        min_length=3,
        max_length=2000,
        examples=[
            "Explain the leave policy."
        ],
    )

    department: Optional[str] = Field(
        default=None,
        examples=["HR"],
    )

    top_k: int = Field(
        default=5,
        ge=1,
        le=20,
    )


class UploadRequest(BaseModel):
    """
    Optional upload metadata.
    """

    department: Optional[str] = None

    author: Optional[str] = None

    version: Optional[str] = "1.0"
