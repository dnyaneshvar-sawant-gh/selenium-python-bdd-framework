import logging

def loggen():
    logger = logging.getLogger("OrangeHRM")
    file_handler = logging.FileHandler("logs/test.log")
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)
    return logger
