"""
Photo Scanner — Metadata Scorer (Public Interface)

Scores how well a photo's metadata matches a search query.
The production implementation uses multi-dimensional matching across:
- Temporal expressions (dates, seasons, relative time like "last week")
- Location matching (city/state/country from reverse-geocoded GPS)
- Device identification ("iPhone 15", "Samsung Galaxy")
- Camera settings (ISO, aperture, shutter speed)
- Scene attributes (indoor/outdoor, natural/urban)
- Color attributes (dominant colors, warm/cool tone)
- Quality attributes (blurry, well-exposed, etc.)

This is a core proprietary scoring engine with ~600 lines of matching logic.
"""

from typing import List, Tuple


def score_batch_metadata(query: str, metadata_list: list) -> Tuple[List[float], List[List[str]]]:
    """
    Score how well each metadata entry matches the query.

    Args:
        query: The user's search query string
        metadata_list: List of metadata dicts (one per photo)

    Returns:
        scores: List of float scores (0.0 = no match, higher = better match)
        reasons: List of lists of string reasons explaining each score
    """
    print(f"[TEASER] Would score {len(metadata_list)} metadata entries against: '{query}'")
    return [0.0] * len(metadata_list), [[]] * len(metadata_list)
