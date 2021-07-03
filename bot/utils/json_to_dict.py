
import json


def json_to_dict(json_file_path: str) -> dict:
    with open(json_file_path, 'r') as f:
        data = json.load(f)
    return data
