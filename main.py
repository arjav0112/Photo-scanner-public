"""
Photo Scanner — AI-Powered Local Photo Intelligence Engine (Public Teaser)

This is the CLI entry point for Photo Scanner. In the public teaser,
core engine logic is abstracted to proprietary modules.

For the full implementation, see the private repository.

Commands:
    scan <directory>        Scan a photo directory and build the AI index
    search <query>          Search photos using natural language
    dedupe                  Find and manage duplicate images
    group-faces             Cluster detected faces into person identities
    name-person <id> <name> Assign a name to a person cluster
    search-person <query>   Find all photos containing a specific person
"""

import os
import argparse
from src.scanner import PhotoScanner
from src.database import PhotoDatabase
from src.model_handler import MobileCLIPHandler
from src.metadata_scorer import score_batch_metadata
from src.query_analyzer import QueryAnalyzer
from search_config import SearchConfig
import numpy as np


def main():
    parser = argparse.ArgumentParser(description="Local Photo Scanner & Search")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Scan Command
    scan_parser = subparsers.add_parser("scan", help="Scan a directory for photos")
    scan_parser.add_argument("directory", help="Path to the directory to scan")

    # Search Command
    search_parser = subparsers.add_parser("search", help="Search for photos")
    search_parser.add_argument("query", help="Text query")

    # Dedupe Command
    dedupe_parser = subparsers.add_parser("dedupe", help="Find and manage duplicate images")
    dedupe_parser.add_argument(
        "--phash-threshold", type=int, default=10,
        help="Hamming distance threshold for pHash matching (default: 10, 0=pixel-identical)"
    )
    dedupe_parser.add_argument(
        "--embedding-threshold", type=float, default=0.90,
        help="Cosine similarity threshold for embedding-based matching (default: 0.90)"
    )
    dedupe_parser.add_argument(
        "--no-embedding", action="store_true",
        help="Skip CLIP embedding similarity check (faster, pHash only)"
    )
    dedupe_parser.add_argument(
        "--auto-mark", action="store_true",
        help="Automatically mark duplicates in the database without interactive review"
    )
    dedupe_parser.add_argument(
        "--delete", action="store_true",
        help="Delete duplicate files from disk (IRREVERSIBLE — use with caution)"
    )
    dedupe_parser.add_argument(
        "--list", action="store_true",
        help="List all previously marked duplicates stored in the database"
    )

    # Face Grouping Commands
    group_faces_parser = subparsers.add_parser(
        "group-faces", help="Cluster all detected faces into person identities"
    )
    group_faces_parser.add_argument(
        "--reset", action="store_true",
        help="Wipe existing person assignments and recluster from scratch"
    )

    name_person_parser = subparsers.add_parser(
        "name-person", help="Assign a name to a person cluster"
    )
    name_person_parser.add_argument("person_id", type=int, help="Person ID from group-faces output")
    name_person_parser.add_argument("name", help="Human-readable name for this person")

    search_person_parser = subparsers.add_parser(
        "search-person", help="List all photos containing a specific person"
    )
    search_person_parser.add_argument(
        "person", help="Person name or numeric ID"
    )

    args = parser.parse_args()

    if args.command == "scan":
        print("[Photo Scanner] Initializing Scanner...")
        print("[TEASER MODE] Core scanning engine is proprietary.")
        print("[TEASER MODE] In production, this would:")
        print("  → Load CLIP ViT-B-32 model for visual embeddings")
        print("  → Initialize PaddleOCR for text extraction")
        print("  → Initialize YOLOv8n for object/scene detection")
        print("  → Initialize InsightFace for face detection")
        print("  → Scan directory recursively with incremental indexing")
        print("  → Process in parallel batches of 16 images")
        print("  → Store embeddings, metadata, OCR text, and face data in SQLite")
        print("  → Build FAISS vector index for fast search")

    elif args.command == "search":
        print(f"[Photo Scanner] Searching for: '{args.query}'")
        print("[TEASER MODE] Core search engine is proprietary.")
        print("[TEASER MODE] In production, this would:")
        print("  → Analyze query intent (metadata/visual/text/hybrid)")
        print("  → Calculate dynamic weights per signal type")
        print("  → Generate text embedding via CLIP")
        print("  → Search FAISS index for visual candidates")
        print("  → Score OCR matches with token-level fuzzy matching")
        print("  → Score metadata matches (date, location, device, scene)")
        print("  → Fuse scores with intent-weighted formula")
        print("  → Apply adaptive feedback penalties/boosts")
        print("  → Filter with gap detection + proportional thresholding")
        print("  → Return ranked results with score breakdown")

    elif args.command == "dedupe":
        print("[Photo Scanner] Running duplicate detection...")
        print("[TEASER MODE] Core dedup engine is proprietary.")
        print("[TEASER MODE] In production, this would:")
        print("  → Compute perceptual hashes for all images")
        print("  → Compare Hamming distances for near-exact matches")
        print("  → Compare CLIP embedding cosine similarity for semantic matches")
        print("  → Group duplicates as EXACT / NEAR_EXACT / SEMANTIC")
        print("  → Launch interactive review mode")

    elif args.command == "group-faces":
        print("[Photo Scanner] Running face clustering...")
        print("[TEASER MODE] Core face engine is proprietary.")
        print("[TEASER MODE] In production, this would:")
        print("  → Load all face embeddings from database")
        print("  → Run DBSCAN clustering with graph merging")
        print("  → Create person entries with representative faces")
        print("  → Display person IDs with photo counts")

    elif args.command == "name-person":
        print(f"[Photo Scanner] Naming person {args.person_id} → '{args.name}'")
        print("[TEASER MODE] Database write is proprietary.")

    elif args.command == "search-person":
        print(f"[Photo Scanner] Searching for person: '{args.person}'")
        print("[TEASER MODE] Person search is proprietary.")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
