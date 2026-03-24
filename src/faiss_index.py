"""
Photo Scanner — FAISS Vector Index (Public Interface)

Manages the FAISS approximate nearest-neighbor index for fast
embedding search. Production uses FAISS IndexFlatIP (inner product)
for cosine similarity search after L2 normalization.

Performance: Sub-millisecond search across 10,000+ embeddings.
Storage: faiss_index.bin + faiss_id_map.npy for persistent index.
"""

import numpy as np
from typing import Tuple


class FAISSIndex:
    """
    FAISS-based vector search index.

    Production features:
    - IndexFlatIP for exact inner-product search
    - ID mapping between FAISS positions and database IDs
    - Persistent save/load to disk
    - Automatic rebuild on scan changes
    """

    def __init__(self, index_path: str = "faiss_index.bin", id_map_path: str = "faiss_id_map.npy"):
        self.index_path = index_path
        self.id_map_path = id_map_path
        print("[TEASER] FAISSIndex initialized")

    def build_index(self, ids: np.ndarray, embeddings: np.ndarray):
        """Build a new FAISS index from database embeddings."""
        print(f"[TEASER] Would build FAISS index with {len(ids)} vectors")

    def load_or_build(self, db):
        """Load existing index from disk, or build from database."""
        print("[TEASER] Would load/build FAISS index")

    def search(self, query_embedding: np.ndarray, top_k: int = 100) -> Tuple[np.ndarray, np.ndarray]:
        """
        Search the index for nearest neighbors.

        Returns:
            (ids, scores): Database IDs and similarity scores for top-k matches
        """
        print(f"[TEASER] Would search FAISS index (top_k={top_k})")
        return np.array([], dtype=np.int64), np.array([], dtype=np.float32)

    def save(self):
        """Persist index and ID map to disk."""
        print("[TEASER] Would save FAISS index to disk")
