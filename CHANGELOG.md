# Changelog

All notable changes to the Photo Scanner project will be documented in this file.

## [v0.8.0] - 2026-03-22
### Added
- **Face Recognition Suite**: InsightFace ArcFace detection with 512-dim embeddings.
- **Person Clustering**: DBSCAN + graph merge for unsupervised identity grouping.
- **Incremental Assignment**: New faces auto-assigned to existing person clusters during scan.
- **CLI Commands**: `group-faces`, `name-person`, `search-person` for person management.

### Changed
- Scanner now processes faces in parallel with metadata and OCR extraction.
- Database schema extended with `persons` and `faces` tables.

## [v0.7.0] - 2026-03-18
### Added
- **Duplicate Detection Engine**: Multi-method duplicate identification system.
- **Perceptual Hashing (pHash)**: Fast Hamming-distance comparison for near-exact duplicates.
- **Semantic Duplicate Detection**: CLIP embedding cosine similarity for visually similar images.
- **Interactive Dedup CLI**: Review, mark, skip, or delete duplicates with full control.
- **Configurable Thresholds**: Adjustable pHash and embedding similarity thresholds.

### Fixed
- Resolved pHash computation edge cases with corrupted image files.
- Fixed embedding threshold normalization for consistent similarity scores.

## [v0.6.0] - 2026-03-15
### Added
- **FAISS Vector Indexing**: Sub-millisecond approximate nearest-neighbor search.
- **Adaptive Feedback System**: Feedback-driven scoring with per-result penalties and boosts.
- **Feedback Statistics CLI**: Track and analyze search quality metrics.

### Changed
- Migrated from brute-force cosine similarity to FAISS IndexFlatIP — 50x speedup.
- Search results now include feedback-adjusted scores.

## [v0.5.0] - 2026-03-10
### Added
- **Intent-Aware Query Analyzer**: Classifies queries into metadata/visual/text/hybrid intents.
- **Dynamic Weight System**: Automatic weight adjustment based on query intent.
- **Search Configuration Module**: Centralized tunable parameters for search behavior.

### Changed
- Search scoring now uses dynamically weighted multi-signal fusion instead of fixed weights.

## [v0.4.0] - 2026-03-05
### Added
- **Metadata Scorer v2**: Deep EXIF extraction with GPS, device, camera settings support.
- **Offline Reverse Geocoding**: GPS coordinate to city/state/country resolution.
- **Color & Scene Analysis**: HSV histogram analysis, scene classification, quality scoring.

## [v0.3.0] - 2026-02-28
### Added
- **PaddleOCR Integration**: High-accuracy text extraction from photos.
- **Document Gatekeeper**: CLIP-based classifier to selectively run OCR only on text-heavy images.
- **OCR Token Matching**: Exact, partial, and fuzzy token matching for text-in-image search.

### Changed
- Migrated from EasyOCR to PaddleOCR for 3x faster extraction with better accuracy.

## [v0.2.0] - 2026-02-20
### Added
- **Incremental Scanning**: Only process new/modified files — skip unchanged photos.
- **Batch Processing**: Multi-threaded parallel processing for metadata, visual, and OCR analysis.
- **SQLite Database**: Persistent storage with automatic schema migration.

## [v0.1.0] - 2026-02-10
### Added
- **Photo Scanner Alpha Launch**: Basic CLIP-based visual search.
- **SentenceTransformer CLIP**: clip-ViT-B-32 model for image and text embeddings.
- **CLI Interface**: `scan` and `search` commands for directory indexing and querying.

---
*For the latest updates, follow the repository.*
