#"import" module uses to import various modules to your code.
# os enabling work with folders and paths
import os
# json enabling the option to load and save files in json format
import json
# def function to create "get_user_input" to collect all the input.
def get_user_input():
# machines to create an empty list to save all the machines
    machines = []
    # the loop will run endlessly until user will break it by typing 'done'
    while True:
        # input asks user to type machine name
        name = input("Enter Machine Name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        os = input("Enter OS (Ubuntu/OS): ")
        cpu = input("Enter CPU (e.g. Intel Core XXX, AMD Ryzen XXX): ")
        ram = input("Enter RAM Capacity (e.g. 4GB): ")
        # creating dictionary with the VM details
        instance_data = {"name": name, "os": os, "cpu": cpu, "ram": ram}
        # adds the dictionary to VMs list
        machines.append(instance_data)
        # function returns all VMs that user defined 
    return machines

# Save information to json file in configs folder
instances = []
if os.path.exists("configs/instances.json"):
    with open("configs/instances.json", "r") as f:
        try:
            instances = json.load(f)
        except json.JSONDecodeError:
            instances = []

new_instances = get_user_input()
instances.extend(new_instances)

with open("configs/instances.json", "w") as f:
    json.dump(instances, f, indent=4)
