# CLOCer

This is a Python program to get the source lines of code (SLOC) count for a given GitHub repository.

This package uses [CLOC](https://github.com/AlDanial/cloc) under the hood and currently only supports Linux systems.

## Example

```python
from clocer import CLOCer

if __name__ == "__main__":
    CLOCer.run("https://github.com/Niweera/CLOCer")
```

The output will be saved in a JSON file as `/clocer/output/Niweera_CLOCer.json`.