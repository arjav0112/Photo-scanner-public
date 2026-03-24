"""
Photo Scanner — Feedback Handler (Public Interface)

Manages user feedback collection and result-level penalty/boost calculations.
Production stores feedback in a separate SQLite database (feedback.db)
and uses it to adjust search result rankings for future queries.

Feedback types: CLICKED, POSITIVE, NEGATIVE
The adaptive learning engine uses these signals to:
- Boost results that receive positive feedback
- Penalize results that receive negative feedback
- Track per-query-intent success rates
"""

from enum import Enum
from typing import Dict, Optional


class FeedbackType(Enum):
    """Types of user feedback on search results."""
    CLICKED = "clicked"
    POSITIVE = "positive"
    NEGATIVE = "negative"


class FeedbackHandler:
    """
    Records and processes user feedback on search results.

    Production features:
    - SQLite-backed feedback storage
    - Per-result penalty/boost calculation
    - Per-intent success rate tracking
    - Configurable decay for old feedback
    """

    def __init__(self, db_path: str = "feedback.db"):
        self.db_path = db_path
        print(f"[TEASER] FeedbackHandler initialized (db: {db_path})")

    def record_feedback(self, query: str, query_intent: str, weights_used: dict,
                       result_path: str, result_rank: int, result_scores: dict,
                       feedback_type: FeedbackType):
        """Record a piece of user feedback on a search result."""
        print(f"[TEASER] Would record {feedback_type.value} feedback")

    def get_result_penalty(self, result_path: str, query: str) -> float:
        """
        Get the penalty/boost multiplier for a specific result.
        
        Returns:
            float: Multiplier (< 1.0 = penalty, > 1.0 = boost, 1.0 = neutral)
        """
        return 1.0

    def get_feedback_stats(self) -> dict:
        """Get aggregate feedback statistics."""
        return {'total_feedback': 0, 'by_intent': {}, 'by_type': {}}
