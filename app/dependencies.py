from functools import lru_cache

from rag.pipeline import RAGPipeline


@lru_cache(maxsize=1)
def get_pipeline():

    """
    Singleton RAG Pipeline
    """

    return RAGPipeline()
