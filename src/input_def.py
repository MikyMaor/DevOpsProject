from pydantic import ValidationError
from src.machine import Machine
from src.logger import provisioning_logger

def get_user_input():
    machines = []

    while True:
        try:
            name = input("Enter Machine Name (or 'Done' to finish): ")
            if name.lower() == "done":
                provisioning_logger.info("User finished entering machines.")
                break

            os_val = input("Enter OS (Windows/Linux): ")
            cpu_val = input("Enter CPU (e.g., Intel Core XXX, AMD Ryzen XXX): ")
            ram_val = input("Enter RAM Capacity (e.g. 4GB): ")

            # Validation
            machine = Machine(
                name=name,
                os=os_val,
                cpu=cpu_val,
                ram=ram_val
            )

            # Machine-specific log
            machine.log_creation()

            # Provisioning log
            provisioning_logger.info(f"Machine '{name}' added successfully.")

            machines.append(machine.to_dict())

        except ValidationError as e:
            provisioning_logger.error("User entered INVALID INPUT.")
            print("\n❌ Invalid input:")
            for err in e.errors():
                print(f" - {err['msg']}")
            print()

        except Exception as e:
            provisioning_logger.error(f"Unexpected error: {e}")
            print("\n❌ Unexpected error occurred. Try again.\n")

    return machines