from pathlib import Path

from fastapi import APIRouter
from fastapi import File
from fastapi import UploadFile

from app.services.document_service import DocumentService

router = APIRouter()


UPLOAD_DIR = Path("data")

UPLOAD_DIR.mkdir(exist_ok=True)


@router.post("/upload")
async def upload_document(

    file: UploadFile = File(...)

):

    filepath = UPLOAD_DIR / file.filename

    with open(filepath, "wb") as f:

        f.write(await file.read())

    service = DocumentService()

    service.ingest(

        str(filepath)

    )

    return {

        "success": True,

        "filename": file.filename

    }
