"""
Photo Scanner — Query Analyzer (Public Interface)

Classifies search queries into intent categories and calculates
dynamic weights for the multi-signal fusion scoring engine.

Intent Categories:
    METADATA_DOMINANT  — queries about time, location, device, camera settings
    VISUAL_DOMINANT    — queries about scene content, objects, colors, mood
    TEXT_DOMINANT       — queries seeking text within images (OCR)
    HYBRID_BALANCED    — queries combining multiple signal types

The production implementation uses keyword pattern matching, temporal
expression parsing, location detection, and semantic analysis to
classify intent with high accuracy. The weight calculation engine
then selects and fine-tunes preset weights based on the classified intent.

This is a core proprietary component of Photo Scanner's search intelligence.
"""

from enum import Enum
from typing import Tuple, Dict, List


class QueryIntent(Enum):
    """Classification of search query intent."""
    METADATA_DOMINANT = "metadata_dominant"
    VISUAL_DOMINANT = "visual_dominant"
    TEXT_DOMINANT = "text_dominant"
    HYBRID_BALANCED = "hybrid_balanced"


class QueryAnalyzer:
    """
    Analyzes search queries to determine intent and calculate dynamic weights.

    Production features:
    - Temporal expression detection (dates, seasons, relative time)
    - Location/place name detection
    - Device/camera model detection
    - OCR-indicative keyword detection
    - Visual content keyword classification
    - Hybrid intent resolution for multi-signal queries
    """

    def __init__(self, weight_presets: dict):
        self.weight_presets = weight_presets
        print("[TEASER] QueryAnalyzer initialized")
        print("[TEASER] Intent classification logic is proprietary")

    def analyze_query(self, query: str) -> Tuple[QueryIntent, Dict[str, float], dict]:
        """
        Analyze a query and return (intent, weights, debug_info).

        Returns:
            intent: QueryIntent enum value
            weights: Dict with 'visual', 'ocr', 'metadata' weights (sum ~1.0)
            debug_info: Dict with 'reason' explaining the classification
        """
        print(f"[TEASER] Would analyze query intent: '{query}'")
        return (
            QueryIntent.VISUAL_DOMINANT,
            {'visual': 0.7, 'ocr': 0.2, 'metadata': 0.1},
            {'reason': '[TEASER] Default visual-dominant classification'}
        )

    def get_ocr_tokens(self, query: str) -> List[str]:
        """
        Extract tokens suitable for OCR matching from the query.
        Filters out stop words and short tokens.
        """
        return query.lower().split()
