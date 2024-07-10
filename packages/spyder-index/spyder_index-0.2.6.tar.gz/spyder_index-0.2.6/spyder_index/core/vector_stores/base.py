from typing import Optional
from spyder_index.core.document import Document

class VectorStoreQueryResult:
    """Vector store query result."""

    document: Optional[Document] = None
    confidence: Optional[float] = None
