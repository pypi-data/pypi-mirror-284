from typing import Any, List, Literal

from spyder_index.core.document import Document
from spyder_index.core.embeddings import Embeddings

from pydantic.v1 import BaseModel, PrivateAttr

class HuggingFaceEmbeddings(BaseModel, Embeddings):
    """HuggingFace sentence_transformers embedding models."""

    model_name: str = "sentence-transformers/all-MiniLM-L6-v2"
    device: Literal["cpu", "cuda"] = "cpu"

    _client: Any = PrivateAttr()

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        from sentence_transformers import SentenceTransformer

        self._client = SentenceTransformer(self.model_name, device=self.device)

    def get_query_embedding(self, query: str) -> List[float]:
        """Compute embedding for a text.

        Args:
            query (str): Input query to compute embedding.

        Returns:
            List[float]: Embedding vector for the input text.
        """ 
        embedding_text = self.get_texts_embedding([query])[0]

        return embedding_text

    def get_texts_embedding(self, texts: List[str]) -> List[List[float]]:
        """Compute embeddings for list of texts.

        Args:
            texts (List[str]): List of input texts to compute embedding.

        Returns:
            List[List[float]]: List of embedding vectors for the input texts.
        """
        embedding_texts = self._client.encode(texts)

        return embedding_texts
    
    def get_documents_embedding(self, documents: List[Document]) -> List[List[float]]:
        """Compute embeddings for a list of documents.

        Args:
            documents (List[Document]): List of Document.

        Returns:
            List[List[float]]: List of embedding vectors for the input documents.
        """

        texts = [document.get_content() for document in documents]
        embedding_documents = self.get_texts_embedding(texts)

        return embedding_documents
