Yes, that code should be included in the `README.md` file under the usage section to demonstrate how to use the library. Here's the updated `README.md` content:

### `README.md`

```markdown
# HudUtils

A utility library for flattening JSON data.

## Installation

```bash
pip install hudutils
```

## Usage

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
```

This example shows users how to import and use the `flatten_json` function from your `hudutils` library. It provides a clear and practical example of how to use the library in their own projects.
