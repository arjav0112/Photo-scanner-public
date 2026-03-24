# Photo Scanner Security Model v1.0

## 1. Local-Only Architecture
Photo Scanner operates on the principle that your photo library should never leave your physical hardware.

### Data Flow Specification:
1. **Scanning**: Photos are read from disk into memory for analysis.
2. **Embedding Generation**: CLIP model runs locally to generate 512-dim vectors.
3. **Storage**: All embeddings, metadata, and face data are stored in local SQLite databases.
4. **Search**: FAISS index performs vector similarity search entirely in-process.

**Network Usage**: The ONLY network call is the initial model download from HuggingFace (one-time). After that, the system operates 100% offline.

## 2. Database Security
- SQLite databases (`photos.db`, `feedback.db`) contain only derived data (embeddings, metadata).
- No raw photo data is stored in the database — only file paths and computed features.
- FAISS index files (`faiss_index.bin`, `faiss_id_map.npy`) contain numerical vectors only.

## 3. Model Security
- CLIP model weights are cached locally in `assets/local_clip_model/` after first download.
- InsightFace models are cached in the user's home directory (standard InsightFace behavior).
- No model telemetry or usage tracking is implemented.

## 4. Face Data Protection
Face embeddings are mathematical vectors derived from facial features. They cannot be used to reconstruct the original face image. However, they can potentially identify individuals across photos, so they are stored locally with the same protections as all other data.

---
**Arjav Jain**  
*Photo Scanner Security Lead*
