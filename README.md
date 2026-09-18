# Python Basics

A single path through Python, in order. One topic per cell, with the result in a comment — the format from [Mosh's beginner course](https://www.youtube.com/watch?v=K5KVEU3aaeQ).

This covers **Phase 1** of the data career roadmap (Python fluency), plus a pandas preview.

## How to use it

1. Open the numbered files **in order**. Do not skip.
2. Run each cell. Read the comment on the right — that is the expected output.
3. Change a value and re-run. If you cannot predict the new output, you do not know it yet.
4. Use the `pro` conda env (Python 3.11, pandas and requests already installed).

## Path

| # | File | What you learn |
|---|---|---|
| 01 | [01_python_basics.ipynb](01_python_basics.ipynb) | print, variables, strings, numbers, `if` |
| 02 | [02_loops_and_functions.ipynb](02_loops_and_functions.ipynb) | `while` / `for`, functions, comprehensions |
| 03 | [03_data_structures.ipynb](03_data_structures.ipynb) | lists, tuples, sets, dicts, nested JSON |
| 04 | [04_classes.ipynb](04_classes.ipynb) | classes, `__init__`, dataclasses |
| 05 | [05_argparse.py](05_argparse.py) | scripts, `argparse`, `if __name__ == "__main__"` |
| 06 | [06_requests.ipynb](06_requests.ipynb) | HTTP GET, status codes, JSON, saving a file |
| 07 | [07_pandas.ipynb](07_pandas.ipynb) | Series, DataFrame, filter, groupby, CSV |

Run the script from a terminal:

```bash
python 05_argparse.py --name Fath --baths 5 --bedrooms 10 --kitchens 5
```

## What comes after

Files, `pathlib`, error handling, type hints, and `pytest` are the rest of Phase 1. They are not in this repo yet — they belong with the command-line API tool you will ship in `data-portfolio`.
