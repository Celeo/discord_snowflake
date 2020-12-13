# snowflake

[![CI](https://github.com/Celeo/snowflake/workflows/CI/badge.svg?branch=master)](https://github.com/Celeo/snowflake/actions?query=workflow%3ACI)
[![Python version](https://img.shields.io/badge/Python-3.7+-blue)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

Simple implementation of the Discord Snowflake API.

## Installing

1. Install [poetry](https://python-poetry.org/)
1. Clone the repo
1. Install dependencies with `poetry install`

## Using

TBD

## Developing

### Building

### Requirements

* Git
* Poetry
* Python 3.9

### Steps

```sh
git clone https://github.com/Celeo/snowflake
cd snowflake
poetry install
```

### Running tests

| | |
| --- | --- |
| No coverage | `poetry run pytest`
| Coverage printout | `poetry run pytest --cov=snowflake` |
| Coverage report | `poetry run pytest --cov=snowflake --cov-report=html` |

## License

Licensed under MIT ([LICENSE](LICENSE)).

## Contributing

Please feel free to contribute. Please open an issue first (or comment on an existing one) so that I know that you want to add/change something.

Unless you explicitly state otherwise, any contribution intentionally submitted for inclusion in the work by you, as defined in the Apache-2.0 license,
shall be dual licensed as above, without any additional terms or conditions.
