"""
Photo Scanner — Database Layer (Public Interface)

Manages SQLite storage for photos, embeddings, faces, and person clusters.
The production implementation includes:
- Automatic schema migration for evolving features
- Binary blob storage for numpy embeddings (float32)
- JSON-serialized metadata storage
- Efficient batch retrieval for FAISS index building
- Full CRUD for photos, faces, persons, and duplicates

Schema:
    photos:  id, path, filename, size_bytes, modified_time, embedding, metadata, ocr_text, phash, is_duplicate, duplicate_of
    faces:   id, photo_id, person_id, bbox (x1,y1,x2,y2), det_score, embedding, age_estimate, gender
    persons: id, name, representative_face_id, created_at, updated_at
"""

import numpy as np
from typing import List, Tuple, Optional


class PhotoDatabase:
    """
    SQLite database manager for Photo Scanner.

    Handles all persistent storage including:
    - Photo records with embeddings and metadata
    - Face detection results with ArcFace embeddings
    - Person cluster assignments
    - Duplicate detection flags
    """

    def __init__(self, db_path: str = "photos.db"):
        self.db_path = db_path
        print(f"[TEASER] PhotoDatabase initialized (path: {db_path})")
        print("[TEASER] Production auto-migrates schema on init")

    def add_photo(self, path: str, size: int, mtime: float,
                  embedding: np.ndarray, metadata: dict = None, ocr_text: str = ""):
        """Add a photo with its CLIP embedding and metadata to the database."""
        print(f"[TEASER] Would store photo: {path}")

    def update_photo(self, path: str, size: int, mtime: float,
                     embedding: np.ndarray, metadata: dict = None, ocr_text: str = ""):
        """Update an existing photo entry (for incremental re-scanning)."""
        print(f"[TEASER] Would update photo: {path}")

    def get_all_embeddings(self) -> Tuple[List[str], np.ndarray]:
        """Retrieves all embeddings and their corresponding paths."""
        return [], np.array([], dtype=np.float32)

    def get_all_embeddings_with_ids(self) -> Tuple[np.ndarray, np.ndarray]:
        """Retrieve all (id, embedding) pairs for FAISS index building."""
        return np.array([], dtype=np.int64), np.array([], dtype=np.float32)

    def get_batch_by_ids(self, ids: list) -> list:
        """Retrieve photo data for specific database IDs (post-FAISS search)."""
        return []

    def get_photo_count(self) -> int:
        """Get total number of photos with embeddings."""
        return 0

    def get_scanned_paths_with_mtime(self) -> dict:
        """Returns dict of {path: (modified_time, size_bytes)} for change detection."""
        return {}

    def remove_photos(self, paths: list):
        """Remove photos that no longer exist on disk."""
        pass

    def update_phash(self, path: str, phash_bytes: bytes):
        """Store the perceptual hash blob for a photo."""
        pass

    def get_all_for_dedup(self) -> List[dict]:
        """Retrieve all photos with id, path, size_bytes, phash, and embedding."""
        return []

    def mark_as_duplicate(self, path: str, original_path: str):
        """Flag a photo as a duplicate of another."""
        pass

    def get_duplicates(self) -> List[dict]:
        """Return all photos currently flagged as duplicates."""
        return []

    def delete_photos_by_path(self, paths: List[str]):
        """Permanently delete photo records from the database."""
        pass

    # === Face / Person CRUD ===

    def get_photo_id(self, path: str) -> Optional[int]:
        """Return the integer PK for a photo path, or None."""
        return None

    def add_face(self, photo_id: int, bbox: list, det_score: float,
                 embedding: np.ndarray, age: Optional[int] = None,
                 gender: Optional[str] = None) -> int:
        """Insert a face record; returns the new face id."""
        return 0

    def delete_faces_for_photo(self, photo_id: int):
        """Remove all face rows for a given photo (used on rescan)."""
        pass

    def get_all_faces_with_embeddings(self) -> List[dict]:
        """Return all face rows with embeddings for clustering."""
        return []

    def update_face_person(self, face_id: int, person_id: Optional[int]):
        """Assign a person_id to a face row."""
        pass

    def add_person(self, name: Optional[str] = None, rep_face_id: Optional[int] = None) -> int:
        """Insert a new person; returns new person id."""
        return 0

    def update_person_name(self, person_id: int, name: str):
        """Assign a human-readable name to a person cluster."""
        pass

    def get_persons(self) -> List[dict]:
        """Return all persons with face counts."""
        return []

    def get_photos_for_person(self, person_id: int) -> List[str]:
        """Return distinct photo paths containing a given person."""
        return []

    def get_person_centroids(self) -> dict:
        """Return {person_id: centroid_embedding} for incremental assignment."""
        return {}

    def delete_all_persons(self):
        """Wipe persons table and person_id assignments (for full recluster)."""
        pass
