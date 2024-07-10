from typing import Literal, List

from spyder_index.core.document import Document
from spyder_index.core.embeddings import Embeddings
from pydantic.v1 import BaseModel

from langchain_experimental.text_splitter import SemanticChunker

class SemanticSplitter(BaseModel):

    embed_model: Embeddings
    buffer_size: int = 1
    breakpoint_threshold_amount: int = 95
    device: Literal["cpu", "cuda"] = "cpu"

    class Config:
        arbitrary_types_allowed = True

    def from_text(self, text: str) -> List[str]: 
        """
        Split text into chunks.
        
        Args:
        - text (str): Input text to split.
        
        Returns:
        - List[str]: List of chunks.
        """
        text_splitter = SemanticChunker(
            embeddings=self.embed_model,
            buffer_size=self.buffer_size, 
            breakpoint_threshold_amount=self.breakpoint_threshold_amount)
        
        return text_splitter.split_text(text)
    
    def from_documents(self, documents: List[Document]) -> List[Document]:    
        """
        Split documents into chunks.
        
        Args:
        - documents (List[Document]): List of Documents
        
        Returns:
        - List[Document]: List of Document split into chunks.
        """ 
        chunks = []
        
        for document in documents:
            texts = self.from_text(document.get_content())

            for text in texts:
                chunks.append(Document(text=text, metadata=document.get_metadata()))

        return chunks
    