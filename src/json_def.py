import json

# Function to save machine configurations to a JSON file.
def save_to_json(data, path="configs/instances.json"):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    print(f"\n✔ Saved to {path} ✅ ")