from pathlib import Path


def run_training(experiment_name: str) -> None:
    """Placeholder training launcher."""
    project_root = Path(__file__).resolve().parents[3]
    output_dir = project_root / "outputs" / "logs"
    print(
        f"[samplegen] Training placeholder for '{experiment_name}'. "
        f"Logs dir: {output_dir}"
    )
