
import logging
import os
from src.input_def import get_user_input
from src.json_def import save_to_json
from src.installer_def import run_install_script

# define provisioning logger and log file path.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)

PROV_LOG_PATH = os.path.join(LOG_DIR, "provisioning.log")

# set up provisioning logger.
provisioning_logger = logging.getLogger("provisioning_logger")
provisioning_logger.setLevel(logging.INFO)

# ensure no duplicate handlers are added.
if not provisioning_logger.handlers:
    file_handler = logging.FileHandler(PROV_LOG_PATH)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    provisioning_logger.addHandler(file_handler)

provisioning_logger.info("Provisioning script started 🚀")


#  main provisioning workflow
if __name__ == "__main__":

    # get user input for machine configurations
    provisioning_logger.info("Collecting machine input from user...")
    instances = get_user_input()

    # Save configurations to JSON file
    provisioning_logger.info("Saving instances to JSON file...")
    save_to_json(instances)
    provisioning_logger.info("JSON saved successfully.")

    # Run installation script on Linux only
    provisioning_logger.info("Starting NGINX installation script...")
    run_install_script()
    provisioning_logger.info("NGINX installation script finished.")

    provisioning_logger.info("Provisioning script finished successfully ✔️")
    print("\nProvisioning script finished successfully! ✔️")