from typing import List

from pydantic import BaseModel


class Source(BaseModel):

    source: str

    chunk: int

    score: float


class QueryResponse(BaseModel):

    question: str

    answer: str

    confidence: float

    sources: List[Source]


class UploadResponse(BaseModel):

    success: bool

    filename: str


class DocumentResponse(BaseModel):

    source: str

    chunks: int

    document_type: str


class HealthResponse(BaseModel):

    status: str

    timestamp: str

    application: str

    version: str


class ErrorResponse(BaseModel):

    success: bool

    message: str
