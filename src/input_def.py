from src.machine import Machine
import logging

# Function to get user input for machine configurations
def get_user_input(run_script_callback=None):
    machines = []

    while True:
        name = input("Enter Machine Name (or 'Done' to finish): ")
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

            if run_script_callback:
                run_script_callback()

        except Exception as e:
            print(f"\n❌ Invalid input: {e}")
            print("Please try again.\n")

        logging.info(f"User input: name={name}, os={os_val}, cpu={cpu_val}, ram={ram_val}")
        logging.error(f"Validation error: {e}")

    return machines
