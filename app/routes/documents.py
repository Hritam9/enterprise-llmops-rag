from fastapi import APIRouter

from app.services.document_service import DocumentService

router = APIRouter()


@router.get("")
async def list_documents():

    service = DocumentService()

    return service.list_documents()


@router.delete("/{document_id}")
async def delete_document(

    document_id: str

):

    service = DocumentService()

    service.delete_document(

        document_id

    )

    return {

        "deleted": document_id

    }
