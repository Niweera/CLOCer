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

Sample output:

```json
{
  "header": {
    "cloc_url": "github.com/AlDanial/cloc",
    "cloc_version": "1.82",
    "elapsed_seconds": 0.148819923400879,
    "n_files": 10,
    "n_lines": 231,
    "files_per_second": 67.1953040391159,
    "lines_per_second": 1552.21152330358,
    "report_file": "/clocer/output/Niweera_CLOCer.json"
  },
  "Python": {
    "nFiles": 9,
    "blank": 38,
    "comment": 12,
    "code": 176
  },
  "Markdown": {
    "nFiles": 1,
    "blank": 2,
    "comment": 0,
    "code": 3
  },
  "SUM": {
    "blank": 40,
    "comment": 12,
    "code": 179,
    "nFiles": 10
  }
}
```
