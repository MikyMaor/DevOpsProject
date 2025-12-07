# import subprocess
# import os
# import logging

# # Build absolute path to the bash script.
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# SCRIPT_PATH = os.path.join(BASE_DIR, "..", "scripts", "install_service_nginx.sh")

# # Function to run the bash script
# def run_install_script(script_path=SCRIPT_PATH):
#     try:
#         logging.info(f"Running install script: {script_path}")
#         print(f"\n Running installation script 🔧 located at (Linux only): {script_path}")

#         result = subprocess.run(
#             ["bash", script_path],
#             capture_output=True,
#             text=True
#         )

#         logging.info("Bash stdout: " + result.stdout.strip())

#         print("\n--- Bash Script Output ---")
#         print(result.stdout)

#         if result.returncode != 0:
#             logging.error("Script failed: " + result.stderr.strip())
#             print("Nginx Installation script failed! ❌ ")
#             print(result.stderr)
#         else:
#             logging.info("Service installed successfully")

#     except FileNotFoundError:
#         logging.exception("Script file not found")
#         print(f" Bash script not found ❌ at: {script_path}")
#     except Exception as e:
#         logging.exception("Unexpected error while running script")
#         print(f" Unexpected error ❌: {e}")

import platform
import logging
import subprocess
import os

logger = logging.getLogger("provisioning_logger")

def run_install_script():

    # Check if the OS is Linux, else skip installation
    if platform.system().lower() != "linux":
        logger.info("Skipping installation script because OS is not Linux.")
        return False
    # Build absolute path to the bash script.
    script_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "scripts", "install_service_nginx.sh")
    )
    # Check if script exists
    if not os.path.exists(script_path):
        logger.error(f"Script not found at: {script_path}")
        print(f" Bash script not found ❌ at: {script_path}")
        return False

    try:
        result = subprocess.run(
            ["bash", script_path],
            capture_output=True,
            text=True
        )

        print("--- Bash Script Output ---")
        print(result.stdout)
        print(result.stderr)

        if result.returncode == 0:
            logger.info("NGINX installation script completed successfully.")
            return True

        else:
            logger.error("NGINX installation script failed.")
            return False

    except Exception as e:
        logger.error(f"Script execution error: {e}")
        print(" Error running script ❌")
        return False
