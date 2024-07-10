# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['atomic_dict']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'atomic-dict',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Wesley W. Terpstra',
    'author_email': 'wesley@sifive.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
