import logging
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "..", "logs")
os.makedirs(LOG_DIR, exist_ok=True)

PROV_LOG_PATH = os.path.join(LOG_DIR, "provisioning.log")

provisioning_logger = logging.getLogger("provisioning_logger")
provisioning_logger.setLevel(logging.INFO)

if not provisioning_logger.handlers:
    file_handler = logging.FileHandler(PROV_LOG_PATH)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    provisioning_logger.addHandler(file_handler)