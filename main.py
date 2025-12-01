import json
from src.machine import Machine


def get_user_input():
    machines = []

    while True:
        name = input("Enter Machine Name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        os_val = input("Enter OS (Windows/Linux): ")
        cpu_val = input("Enter CPU (e.g. Intel Core XXX, AMD Ryzen XXX): ")
        ram_val = input("Enter RAM Capacity (e.g. 4GB): ")
        
        # Here is where we create the Machine instance and validate 
        try:
            machine = Machine(
                name=name,
                os=os_val,
                cpu=cpu_val,
                ram=ram_val
            )
        # If validation passes, add to list
            machines.append(machine.model_dump())

        except Exception as e:
            print(f"\n❌ Invalid input: {e}")
            print("Please try again.\n")

    return machines


instances = get_user_input()

with open("configs/instances.json", "w") as f:
    json.dump(instances, f, indent=4)

print("\n✔ Data saved to configs/instances.json")
