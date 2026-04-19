from pathlib import Path


def run_data_pipeline() -> None:
    """Placeholder data pipeline entry point."""
    project_root = Path(__file__).resolve().parents[3]
    metadata_dir = project_root / "data" / "metadata"
    print(f"[samplegen] Data pipeline placeholder. Metadata dir: {metadata_dir}")
