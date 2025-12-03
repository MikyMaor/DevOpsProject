import json
import logging
import os
from src.input_def import get_user_input
from src.json_def import save_to_json
from src.installer_def import run_install_script

# Set up logging and collecting information and define log file path.
LOG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs", "provisioning.log")

# Configure logging in provisioning log file.
logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.info("Provisioning script started 🚀")

# if this script is run directly, execute the main functionality. if not, it can be imported without running.
if __name__ == "__main__":
    instances = get_user_input(run_script_callback=run_install_script)
    save_to_json(instances)

    logging.info("Provisioning script finished successfully ✔️")
    print("\nProvisioning script finished successfully! ✔️")
