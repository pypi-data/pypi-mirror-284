# hudutils/hudutils.py

import json

def flatten_json(json_data, parent_key='', sep='.'):
    items = []
    for k, v in json_data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_json(v, new_key, sep=sep).items())
        elif isinstance(v, list):
            for i, item in enumerate(v):
                items.extend(flatten_json({f"{new_key}[{i}]": item}, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

