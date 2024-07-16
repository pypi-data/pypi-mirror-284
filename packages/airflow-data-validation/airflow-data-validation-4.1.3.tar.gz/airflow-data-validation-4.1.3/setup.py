# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['airflow_data_validation']

package_data = \
{'': ['*']}

install_requires = \
['google-cloud-bigquery>=3.0,<4.0', 'requests>=2.0.0,<3.0.0']

setup_kwargs = {
    'name': 'airflow-data-validation',
    'version': '4.1.3',
    'description': '',
    'long_description': '',
    'author': 'sapir.krespil',
    'author_email': 'sapir.krespil@guesty.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/guestyorg/airflow_data_validation',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
