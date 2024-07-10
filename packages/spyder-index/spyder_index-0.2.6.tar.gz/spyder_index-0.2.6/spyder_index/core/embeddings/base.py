import numpy as np

from typing import List, Literal
from abc import ABC, abstractmethod

class Embeddings(ABC):
    """An interface for embedding models."""

    @classmethod
    def class_name(cls) -> str:
        return "Embeddings"
    
    @abstractmethod
    def get_query_embedding(self, query: str) -> List[float]:
        """Get query embedding."""

    @abstractmethod
    def get_texts_embedding(self, texts: List[str]) -> List[List[float]]:
        """Get text embeddings."""

    @abstractmethod
    def get_documents_embedding(self, documents: List[str]) -> List[List[float]]:
        """Get documents embeddings."""

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return self.get_texts_embedding(texts=texts)
    
    @staticmethod
    def similarity(embedding1: List[float], embedding2: List[float], 
                             mode: Literal["cosine", "dot_product", "euclidean"] = "cosine"):
        """Get embedding similarity."""
        if mode == "euclidean":
            return -float(np.linalg.norm(np.array(embedding1) - np.array(embedding2)))
            
        elif mode == "dot_product":
            return np.dot(embedding1, embedding2)
            
        else:
            product = np.dot(embedding1, embedding2)
            norm = np.linalg.norm(embedding1) * np.linalg.norm(embedding2)
            return product / norm        
        