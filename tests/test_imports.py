from samplegen.training.train import run_training


def test_training_entry_is_importable() -> None:
    assert callable(run_training)
