[![codecov](https://codecov.io/gh/Niweera/CLOCer/branch/main/graph/badge.svg?token=XMEL8AB56Q)](https://codecov.io/gh/Niweera/CLOCer)

# CLOCer

This is a Python program to get the source lines of code (SLOC) count for a given GitHub repository.

This package uses [CLOC](https://github.com/AlDanial/cloc) under the hood and currently only supports Linux systems.

## Example

```python
# Run CLOCer once

from clocer import CLOCer

if __name__ == "__main__":
    CLOCer.setup()
    CLOCer.run("https://github.com/Niweera/CLOCer")
```

```python
# Run CLOCer for multiple repositories

from clocer import CLOCer

repos = ["https://github.com/Niweera/CLOCer"]

if __name__ == "__main__":
    CLOCer.setup()
    for repo in repos:
        CLOCer.run(repo)
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
