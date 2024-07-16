import logging
from pycoretoolkit.logger_config import configure_logging


def test_configure_logging():
    configure_logging()
    logger = logging.getLogger()
    assert len(logger.handlers) > 0
