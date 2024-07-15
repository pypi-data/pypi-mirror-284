# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['vsom']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.9.1,<4.0.0',
 'numpy>=1.19.2,<2.0',
 'pandas>=1.1.5,<2.0',
 'pytorch>=1.5.1,<1.10.0',
 'rdkit>=2023.9.1,<2024.0.0',
 'seaborn>=0.13.2,<0.14.0']

setup_kwargs = {
    'name': 'vsom',
    'version': '0.1.5',
    'description': 'the code of virtual screening of organic materials',
    'long_description': None,
    'author': 'su-group',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
