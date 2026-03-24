"""
Photo Scanner — OCR Handler (Public Interface)

Extracts text from images using PaddleOCR.
The production implementation was migrated from EasyOCR to PaddleOCR
for 3x faster extraction with better accuracy. Text extraction is
gated by a "Document Gatekeeper" in the scanner that uses CLIP
similarity to determine if an image is text-heavy before running OCR.

This is a core proprietary component.
"""


class OCRHandler:
    """
    Handles text extraction from images using PaddleOCR.

    Production features:
    - PaddleOCR initialization with English language support
    - Confidence filtering for extracted text
    - Multi-line text concatenation
    - Error recovery for corrupted images
    """

    def __init__(self):
        print("[TEASER] OCRHandler initialized")
        print("[TEASER] Production uses PaddleOCR for high-accuracy text extraction")

    def extract_text(self, image_path: str) -> str:
        """
        Extract text from an image using PaddleOCR.

        Returns concatenated text from all detected text regions.
        Production filters by confidence threshold and orders by position.
        """
        print(f"[TEASER] Would extract text from: {image_path}")
        return ""
