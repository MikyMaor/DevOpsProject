import json
import subprocess
import os
from src.machine import Machine


# Build absolute path to the bash script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPT_PATH = os.path.join(BASE_DIR, "scripts", "install_service_nginx.sh")


def run_install_script(script_path=SCRIPT_PATH):
    try:
        print(f"\n🔧 Running installation script at: {script_path}")

        result = subprocess.run(
            ["bash", script_path],
            capture_output=True,
            text=True
        )

        print("\n--- Bash Script Output ---")
        print(result.stdout)

        if result.returncode != 0:
            print("❌ Installation script failed!")
            print(result.stderr)
        else:
            print("✅ Service installation completed successfully!")

    except FileNotFoundError:
        print(f"❌ Bash script not found at: {script_path}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


def get_user_input():
    machines = []

    while True:
        name = input("Enter Machine Name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        os_val = input("Enter OS (Windows/Linux): ")
        cpu_val = input("Enter CPU (e.g. Intel Core XXX, AMD Ryzen XXX): ")
        ram_val = input("Enter RAM Capacity (e.g. 4GB): ")

        try:
            machine = Machine(
                name=name,
                os=os_val,
                cpu=cpu_val,
                ram=ram_val
            )

            machine.log_creation()
            machines.append(machine.to_dict())

            run_install_script()

        except Exception as e:
            print(f"\n❌ Invalid input: {e}")
            print("Please try again.\n")

    return machines


def save_to_json(data, path="configs/instances.json"):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    print(f"\n✔ Saved to {path}")


if __name__ == "__main__":
    instances = get_user_input()
    save_to_json(instances)

