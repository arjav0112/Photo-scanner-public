"""
Photo Scanner — Face Detector (Public Interface)

Detects faces in photos using InsightFace with RetinaFace detection
and ArcFace embedding generation. Each detected face produces a
512-dim embedding vector suitable for cross-age, cross-expression
person identification and clustering.

The production implementation uses the InsightFace `buffalo_l` model pack
which includes face detection, landmark alignment, and ArcFace recognition.
"""

from typing import List, Dict


def detect_faces(image_path: str) -> List[Dict]:
    """
    Detect all faces in an image and generate embeddings.

    Returns a list of face dicts, each containing:
        - bbox: [x1, y1, x2, y2] bounding box coordinates
        - det_score: float detection confidence (0-1)
        - embedding: np.ndarray of shape (512,) — ArcFace embedding
        - age: int estimated age (optional)
        - gender: str "M" or "F" (optional)

    Production uses InsightFace FaceAnalysis with:
    - Model: buffalo_l (det + recognition + age/gender)
    - Detection threshold: 0.5
    - Input size: (640, 640)
    """
    print(f"[TEASER] Would detect faces in: {image_path}")
    print("[TEASER] Face detection uses InsightFace ArcFace — proprietary pipeline")
    return []
