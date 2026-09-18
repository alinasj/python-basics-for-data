# Python Basics

A single path through Python, then the analyst stack. One topic per cell, with the result in a comment — the format from [Mosh's beginner course](https://www.youtube.com/watch?v=K5KVEU3aaeQ).

Use the `pro` conda env (Python 3.11). pandas and requests are already installed. For 10–11 you may need `conda install matplotlib seaborn duckdb -c conda-forge`.

## How to use it

1. Open the numbered files **in order**. Do not skip.
2. Run each cell. Read the comment on the right — that is the expected output.
3. Change a value and re-run. If you cannot predict the new output, you do not know it yet.

## Path

### Python fluency (01–08)

| # | File | What you learn |
|---|---|---|
| 01 | [01_python_basics.ipynb](01_python_basics.ipynb) | print, variables, strings, numbers, `if` |
| 02 | [02_loops_and_functions.ipynb](02_loops_and_functions.ipynb) | `while` / `for`, functions, comprehensions |
| 03 | [03_data_structures.ipynb](03_data_structures.ipynb) | lists, tuples, sets, dicts, nested JSON |
| 04 | [04_classes.ipynb](04_classes.ipynb) | classes, `__init__`, dataclasses |
| 05 | [05_argparse.py](05_argparse.py) | scripts, `argparse`, `if __name__ == "__main__"` |
| 06 | [06_requests.ipynb](06_requests.ipynb) | HTTP GET, status codes, JSON, saving a file |
| 07 | [07_pandas.ipynb](07_pandas.ipynb) | Series, DataFrame, filter, groupby, CSV |
| 08 | [08_files_and_errors.ipynb](08_files_and_errors.ipynb) | `pathlib`, JSON, CSV, `try/except` |

### Analyst core (09–11)

This is what a data analyst actually does: clean a table, join it, plot it, and query it.

| # | File | What you learn |
|---|---|---|
| 09 | [09_pandas_analysis.ipynb](09_pandas_analysis.ipynb) | missing values, dtypes, datetime, merge, pivot |
| 10 | [10_visualization.ipynb](10_visualization.ipynb) | `describe`, matplotlib, seaborn, correlation |
| 11 | [11_sql_duckdb.ipynb](11_sql_duckdb.ipynb) | SQL in Python with DuckDB: SELECT, GROUP BY, JOIN |

Run the script from a terminal:

```bash
python 05_argparse.py --name Fath --baths 5 --bedrooms 10 --kitchens 5
```

## What is not in this repo (on purpose)

| Skill | Why it is later |
|---|---|
| numpy as a course | pandas sits on it; you will pick it up when a `.values` error forces you to |
| Window functions, CTEs, Postgres | Phase 2 SQL — practice in `.sql` files, then DataLemur |
| scikit-learn / models | Data science track, after you can brief a chart |
| Spark, dbt, Airflow | Data engineering track, after SQL is fluent |
| pytest, type hints | Learn them on the API-to-CSV tool you ship in `data-portfolio` |

Hiring managers read shipped projects, not tutorial notebooks. When 11 feels easy, build something in `data-portfolio` and put SQL next to it.
