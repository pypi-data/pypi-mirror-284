# Python library to crawl user notes from sharkey instances

[![Latest Version on PyPI](https://img.shields.io/pypi/pyversions/sharkey-crawler?style=flat-square)](https://pypi.org/project/sharkey-crawler)
[![GitHub Tests Action Status](https://img.shields.io/github/actions/workflow/status/hexafuchs/sharkey-crawler/run-tests.yml?branch=main&label=tests&style=flat-square)](https://github.com/hexafuchs/sharkey-crawler/actions?query=workflow%3Arun-tests+branch%3Amain)
[![GitHub Code Style Action Status](https://img.shields.io/github/actions/workflow/status/hexafuchs/sharkey-crawler/fix-python-code-style-issues.yml?branch=main&label=code%20style&style=flat-square)](https://github.com/hexafuchs/sharkey-crawler/actions?query=workflow%3A"Fix+Python+code+style+issues"+branch%3Amain)
[![Total Downloads](https://img.shields.io/pypi/dm/sharkey-crawler.svg?style=flat-square)](https://pypi.org/project/sharkey-crawler)

Python wrapper for the `/users/notes` endpoint of Sharkey (and probably also Misskey). You can use this to crawl the 
public posts of a user.

## Installation

You can install the package via poetry (or another tool of your choosing):

```bash
poetry add sharkey-crawler
```

## Usage

```python
from sharkey_crawler import SharkeyServer

SharkeyServer('example.org').user_notes(
    user_id='xxxxxxxxxx',
    allow_partial=True, 
    with_channel_notes=True,
    with_renotes=False,
    with_replies=False,
    with_files=False,
    limit=10,
    since_id=None,
    since_date=None,
    until_id=None,
    until_date=None
)
```

Checkout the docstring for more usage information.

## Testing

```bash
# All
./venv/bin/pytest -m ""

# Unit
./venv/bin/pytest -m "unit"

# Integration
./venv/bin/pytest -m "integration"

# Unit and Integration
./venv/bin/pytest -m "integration or unit"
```

## Development

### Installing flit

```bash
python3 -m venv venv
./venv/bin/python -m pip install --upgrade pip
./venv/bin/python -m pip install flit
./venv/bin/flit install --only-deps --deps develop
```

### Installing new dependencies

Either add the dependency to the optional dependencies, or create a new dependency within the `[project]` namespace, e.g.:

```toml
[project]
...
dependencies = [
    "requests==2.32.3"
]
```

Then, install dependencies with flit:

```bash
./venv/bin/flit install --only-deps --deps develop
# or: ./venv/bin/flit install --only-deps --deps all
```

## Future Development

You might be asking yourself why this project does not expose more endpoints. It could, and it likely will, but 
currently, the endpoints are not well documented and it takes a lot of effort to even add a single endpoint, which 
Sharkey has a lot of. Since Sharkey is not very old and the future is still unclear, I will not take the effort it 
takes to support more endpoints until I have a use case for it or I see great demand. If you want more endpoints, 
there are two recommended solutions for this: 
* open a discussion, so I and possibly other developers can see which endpoints are requested a lot of have an interesting use case
  * also, vote for endpoints you want to see added in the future
* contribute the endpoints yourself

There might also be solutions to automate parts of the development like creating Pydantic classes. If you are interested 
in this, feel free to contribute or open a discussion to organize this.

## Changelog

Please see [CHANGELOG](CHANGELOG.md) for more information on what has changed recently.

## License

The MIT License (MIT). Please see [License File](LICENSE.md) for more information.