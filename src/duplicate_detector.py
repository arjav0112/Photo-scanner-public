"""
Photo Scanner — Duplicate Detector (Public Interface)

Multi-method duplicate image detection using:
1. Perceptual Hashing (pHash) — Hamming distance for near-exact duplicates
2. CLIP Embedding Similarity — Cosine similarity for semantic duplicates

Duplicate categories:
    EXACT       — Hamming distance = 0 (pixel-identical files)
    NEAR_EXACT  — Hamming distance ≤ threshold (JPEG re-saves, minor compression)
    SEMANTIC    — Cosine similarity ≥ threshold (different file, visual match)

The production implementation includes optimized pHash computation using
PIL DCT and efficient pairwise comparison with early termination.
"""

import numpy as np
from typing import List, Optional


def compute_phash(image_path: str) -> Optional[int]:
    """
    Compute the 64-bit perceptual hash of an image.
    
    Production uses PIL to resize to 32x32, convert to grayscale,
    apply DCT, and extract the hash from the low-frequency components.
    
    Returns None if the image cannot be processed.
    """
    print(f"[TEASER] Would compute pHash for: {image_path}")
    return None


def phash_to_bytes(phash_int: int) -> bytes:
    """Convert a 64-bit pHash integer to 8-byte blob for database storage."""
    return phash_int.to_bytes(8, byteorder='big')


def bytes_to_phash(phash_bytes: bytes) -> int:
    """Convert 8-byte blob back to 64-bit pHash integer."""
    return int.from_bytes(phash_bytes, byteorder='big')


class DuplicateDetector:
    """
    Finds duplicate images using pHash and embedding similarity.

    Production features:
    - O(n²) pairwise Hamming distance comparison with early termination
    - CLIP embedding cosine similarity for semantic matching
    - Union-Find grouping for transitive duplicate chains
    - Configurable thresholds per detection method
    """

    def __init__(self, phash_threshold: int = 10, embedding_threshold: float = 0.95):
        self.phash_threshold = phash_threshold
        self.embedding_threshold = embedding_threshold
        print(f"[TEASER] DuplicateDetector initialized")
        print(f"[TEASER] pHash threshold: ≤{phash_threshold} bits, Embedding threshold: ≥{embedding_threshold:.2f}")

    def find_all_duplicates(self, entries: List[dict], use_embedding: bool = True) -> List[dict]:
        """
        Find all duplicate groups in the photo library.

        Args:
            entries: List of dicts with 'path', 'phash', 'embedding' keys
            use_embedding: Whether to also check CLIP embedding similarity

        Returns:
            List of group dicts: {'type': str, 'keep': str, 'remove': [str]}
        """
        print(f"[TEASER] Would find duplicates among {len(entries)} images")
        print("[TEASER] Duplicate detection logic is proprietary")
        return []
