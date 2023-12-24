import sys

from loguru import logger

message_format = (
    '<green>{time:YYYY-MM-DD HH:mm:ss Z}</green> | '
    '<level>{level: <8}</level> | '
    '<cyan>{module}</cyan>.'
    '<cyan>{function}</cyan>:'
    '<cyan>{line}</cyan> - '
    '<level>{message}</level>'
)

logger.remove(0)
logger.add(
    sys.stderr,
    format=message_format,
    level='INFO',
    backtrace=True,
    diagnose=True,
)
