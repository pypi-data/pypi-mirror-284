import pytest
from pycoretoolkit.config_loader import get_config


def test_get_config():
    config = get_config("tests/test_config.yaml")
    assert "source_dir" in config
    assert "destination_dir" in config
    assert "categories" in config


def test_missing_config_file():
    with pytest.raises(FileNotFoundError):
        get_config("tests/missing_config.yaml")
