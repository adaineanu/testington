import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger()
logFormatter = logging.Formatter("%(asctime)s [%(levelname)-8.8s] %(message)s")
fileHandler = RotatingFileHandler(r"libPG.log", maxBytes=1024 * 1024, backupCount=3)  # 1 MB
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)
logger.setLevel(logging.INFO)
