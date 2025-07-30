import logging
import os

def get_logger(name=__name__, log_file='logs/app.log'):
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    ch = logging.StreamHandler()
    fh = logging.FileHandler(log_file)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(ch)
        logger.addHandler(fh)

    return logger
