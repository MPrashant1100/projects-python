import json

def read_json(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {path}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in file: {path}")

def write_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
