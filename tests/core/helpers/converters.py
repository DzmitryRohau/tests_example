import json
import os


def load_json() -> dict:
    with open(os.path.realpath(__file__).replace("core\\helpers\\converters.py", "data\\data.json")) as f:
        return json.load(f)
