import subprocess
import os
import logging

# Build absolute path to the bash script and note the directory structure
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPT_PATH = os.path.join(BASE_DIR, "scripts", "install_service_nginx.sh")

# Function to run the bash script
def run_install_script(script_path=SCRIPT_PATH):
    try:
        logging.info(f"Running install script: {script_path}")
        print(f"\n Running installation script 🔧 located at (Linux only): {script_path}")

        result = subprocess.run(
            ["bash", script_path],
            capture_output=True,
            text=True
        )

        logging.info("Bash stdout: " + result.stdout.strip())

        print("\n--- Bash Script Output ---")
        print(result.stdout)

        if result.returncode != 0:
            logging.error("Script failed: " + result.stderr.strip())
            print("Nginx Installation script failed! ❌ ")
            print(result.stderr)
        else:
            logging.info("Service installed successfully")
            print("Nginx Service installation completed successfully! ✅ ")

    except FileNotFoundError:
        logging.exception("Script file not found")
        print(f" Bash script not found ❌ at: {script_path}")
    except Exception as e:
        logging.exception("Unexpected error while running script")
        print(f" Unexpected error ❌: {e}")
