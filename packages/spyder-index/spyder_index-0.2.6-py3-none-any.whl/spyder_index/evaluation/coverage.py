import numpy as np
from typing import Literal, List

from spyder_index.core.embeddings import Embeddings

from pydantic.v1 import BaseModel

class KnowledgeBaseCoverage(BaseModel):
    """Indicates how much the KnowledgeBase has contributed to the answer's coverage."""

    embed_model: Embeddings
    similarity_mode: Literal["cosine", "dot_product", "euclidean"] = "cosine"
    similarity_threshold: float = 0.8

    class Config:
        arbitrary_types_allowed = True

    def evaluate(self, contexts: List[str], output: str):
                            
        if not contexts or not output:
            raise ValueError("Must provide these parameters [`contexts`, `output`]")
            
        coverage = { "contexts_score": [], "score": 0 }
        output_embedding = self.embed_model.get_query_embedding(output)
            
        for context in contexts:
            context_embedding = self.embed_model.get_query_embedding(context)
            coverage["contexts_score"].append(self.embed_model.similarity(output_embedding, context_embedding, mode=self.similarity_mode))

        coverage["score"] = np.mean(coverage["contexts_score"])
        coverage["passing"] = coverage["score"] >= self.similarity_threshold

        return coverage
            

