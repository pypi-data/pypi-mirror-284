import logging
from pathlib import Path

from ..handlers import get_console_handler, get_logfile_handler
    
def get_logger(
    name:str, 
    level:int = logging.INFO,
    fmt:str = """ \
%(asctime)s%(_msecs)s | %(levelname)s | %(locate)s | %(funcName)s - %(message)s \
""",
    # datefmt:str = Colors.format("%Y-%m-%d %H:%M:%S", Colors.TIME)
    datefmt:str = "%Y-%m-%d %H:%M:%S",
    use_relative_path:bool = False,
) -> logging.Logger:
    
    logfile_handler = get_logfile_handler(
        level = level,
        fmt = fmt,
        datefmt = datefmt,
        use_relative_path = use_relative_path,
    )
    console_handler = get_console_handler(
        level = level,
        fmt = fmt,
        datefmt = datefmt,
        use_relative_path = use_relative_path,
    )

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(logfile_handler)
    logger.addHandler(console_handler)
    return logger

logger = get_logger(__name__, logging.DEBUG)
logger_relative = get_logger(__name__ + "_relative", logging.DEBUG, use_relative_path=True)

if __name__ == '__main__':

    logger.debug("DEBUG")
    logger.info("INFO")
    logger.warning("WARN")
    logger.error("ERROR")
    logger.critical("CRITICAL")