[![PyPI version](https://badge.fury.io/py/Flask-HTTPAuth-stubs.svg)](https://pypi.org/project/Flask-HTTPAuth-stubs)
[![Code on Github](https://img.shields.io/badge/Code-GitHub-brightgreen)](https://github.com/socgnachilderic/assertpy-stubs)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![GitHub last commit](https://img.shields.io/github/last-commit/MartinThoma/Flask-HTTPAuth-stubs)

# assertpy-stubs

Add types for [assertpy](https://pypi.org/project/assertpy/) for mypy or pyright.

## Installation

```
$ pip install assertpy-stubs
```

## Usage

Mypy or pyright will automatically use the type annotations in this package, once it is
installed. You just need to annotate your code:

```python
from assertpy import assert_that


def test_something():
    assert_that(1 + 2).is_equal_to(3)
    assert_that("foobar").is_length(6).starts_with("foo").ends_with("bar")
    assert_that(["a", "b", "c"]).contains("a").does_not_contain("x")
```

For general hints how to use type annotations, please read [Type Annotations in Python 3.8](https://medium.com/analytics-vidhya/type-annotations-in-python-3-8-3b401384403d)
