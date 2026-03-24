"""
Photo Scanner — Search Cache (Public Interface)

Disk-backed cache for text embeddings to avoid redundant model loads.
When a query has been searched before, the cached embedding is reused
instead of loading the CLIP model — saving ~5 seconds of startup time.

Production uses a dict-based cache with TTL expiration and max entry limits.
"""


class SearchCache:
    """
    Caches text embeddings for repeated queries.

    Production features:
    - Disk-backed persistence
    - TTL-based expiration (default: 300 seconds)
    - Max entry limit (default: 50)
    """

    def __init__(self, max_entries: int = 50, ttl_seconds: int = 300):
        self.max_entries = max_entries
        self.ttl_seconds = ttl_seconds
        print("[TEASER] SearchCache initialized")

    def get_text_embedding(self, query: str):
        """Return cached embedding for query, or None if not cached."""
        return None

    def set_text_embedding(self, query: str, embedding):
        """Store embedding in cache for future reuse."""
        pass
