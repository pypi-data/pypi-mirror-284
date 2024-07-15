Certainly! Here is the updated `README.md` file incorporating the new `filename_with_rollover` function:

```markdown
# HudUtils

Regularly used utils.

## Installation

```bash
pip install hudutils
```

## Usage

### Flatten JSON

```python
from hudutils import hudutils

json_data = {
    "a": 1,
    "b": {
        "c": 2,
        "d": {
            "e": 3
        }
    }
}

flattened = hudutils.flatten_json(json_data)
print(flattened)
```

### Filename with Rollover

```python
from hudutils import hudutils

filename = 'log.txt'
new_filename = hudutils.filename_with_rollover(filename, opts=['year', 'month', 'day'])
print(new_filename)
```
```

This example shows users how to import and use the `flatten_json` and `filename_with_rollover` functions from your `hudutils` library. It provides clear and practical examples of how to use the library in their own projects.
