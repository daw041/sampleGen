from pathlib import Path


def run_evaluation() -> None:
    """Placeholder evaluation launcher."""
    project_root = Path(__file__).resolve().parents[3]
    report_dir = project_root / "outputs" / "reports"
    print(f"[samplegen] Evaluation placeholder. Report dir: {report_dir}")
