from pycoretoolkit.api_key_manager import APIKeyManager


def test_api_key_manager():
    manager = APIKeyManager("test_service", "test_key")
    manager.set_api_key("test_api_key")
    assert manager.get_api_key() == "test_api_key"
