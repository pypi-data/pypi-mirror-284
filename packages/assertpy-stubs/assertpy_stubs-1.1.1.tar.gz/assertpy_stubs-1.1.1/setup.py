# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['assertpy-stubs']

package_data = \
{'': ['*']}

install_requires = \
['assertpy>=1.1,<2.0', 'typing-extensions>=4.12.2,<5.0.0']

setup_kwargs = {
    'name': 'assertpy-stubs',
    'version': '1.1.1',
    'description': 'Mypy|Pyright plugin and stubs for assertpy',
    'long_description': '[![PyPI version](https://badge.fury.io/py/Flask-HTTPAuth-stubs.svg)](https://pypi.org/project/Flask-HTTPAuth-stubs)\n[![Code on Github](https://img.shields.io/badge/Code-GitHub-brightgreen)](https://github.com/socgnachilderic/assertpy-stubs)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n![GitHub last commit](https://img.shields.io/github/last-commit/MartinThoma/Flask-HTTPAuth-stubs)\n\n# assertpy-stubs\n\nAdd types for [assertpy](https://pypi.org/project/assertpy/) for mypy or pyright.\n\n## Installation\n\n```\n$ pip install assertpy-stubs\n```\n\n## Usage\n\nMypy or pyright will automatically use the type annotations in this package, once it is\ninstalled. You just need to annotate your code:\n\n```python\nfrom assertpy import assert_that\n\n\ndef test_something():\n    assert_that(1 + 2).is_equal_to(3)\n    assert_that("foobar").is_length(6).starts_with("foo").ends_with("bar")\n    assert_that(["a", "b", "c"]).contains("a").does_not_contain("x")\n```\n\nFor general hints how to use type annotations, please read [Type Annotations in Python 3.8](https://medium.com/analytics-vidhya/type-annotations-in-python-3-8-3b401384403d)\n',
    'author': 'SOCGNA KOUYEM Childeric',
    'author_email': 'socgnachilderic@proton.me',
    'maintainer': 'SOCGNA KOUYEM Childeric',
    'maintainer_email': 'socgnachilderic@proton.me',
    'url': 'https://github.com/socgnachilderic/assertpy-stubs',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9',
}


setup(**setup_kwargs)
