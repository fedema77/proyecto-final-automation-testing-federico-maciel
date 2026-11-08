import json
from pathlib import Path


def load_json(file_name):
    file_path = Path(__file__).resolve().parents[1] / "data" / file_name
    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)
