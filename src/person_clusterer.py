"""
Photo Scanner — Person Clusterer (Public Interface)

Clusters detected face embeddings into person identity groups.
The production implementation uses DBSCAN for initial clustering
followed by graph-based merge to handle fragmented clusters.

For incremental assignment during scanning, new faces are matched
against existing person centroids using cosine similarity.

Clustering parameters:
    eps: 0.6 — DBSCAN neighborhood radius
    min_samples: 2 — minimum faces to form a cluster
    cosine_threshold: 0.55 — minimum similarity for incremental assignment
"""

import numpy as np
from typing import Dict, Optional


def cluster_faces(embeddings: np.ndarray, face_ids: list) -> Dict[int, int]:
    """
    Cluster face embeddings into person groups using DBSCAN.

    Args:
        embeddings: np.ndarray of shape (N, 512) — ArcFace embeddings
        face_ids: list of integer face IDs corresponding to embeddings

    Returns:
        Dict mapping face_id → cluster_label (-1 = unassigned)
    """
    print(f"[TEASER] Would cluster {len(face_ids)} faces")
    print("[TEASER] DBSCAN + graph merge clustering is proprietary")
    return {fid: -1 for fid in face_ids}


def assign_new_face(face_embedding: np.ndarray, person_centroids: dict) -> Optional[int]:
    """
    Assign a new face to the closest existing person cluster.

    Args:
        face_embedding: 512-dim ArcFace embedding for the new face
        person_centroids: dict of {person_id: centroid_embedding}

    Returns:
        person_id if match found (cosine sim > threshold), else None
    """
    print("[TEASER] Would perform incremental face assignment")
    return None


def compute_cluster_centroid(embeddings: np.ndarray) -> np.ndarray:
    """Compute the L2-normalized mean embedding for a cluster."""
    if len(embeddings) == 0:
        return np.zeros(512, dtype=np.float32)
    centroid = embeddings.mean(axis=0)
    norm = np.linalg.norm(centroid)
    if norm > 1e-6:
        centroid /= norm
    return centroid.astype(np.float32)
