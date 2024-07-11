# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['grasp2alm']

package_data = \
{'': ['*']}

install_requires = \
['healpy>=1.15.0,<2.0.0',
 'matplotlib>=3.1,<4.0',
 'numpy>=1.23,<2.0',
 'pytest>=8.1.1,<9.0.0',
 'scipy>=1.13.0,<2.0.0']

setup_kwargs = {
    'name': 'grasp2alm',
    'version': '0.1.1',
    'description': 'Package supporting conversion from GRASP beam format to spherical harmonic coefficients for CMB experiments, conversion to expansion coefficients for spherical harmonics, etc.',
    'long_description': '<p align="center">\n  <h1>\n  <img src="./images/logo/grasp2alm_logo_wide.png" alt="Logo">\n  </h1>\n</p>\n\n[![docs](https://img.shields.io/badge/docs-stable-blue.svg)](https://yusuke-takase.github.io/grasp2alm/index.html)\n[![PyPI - Version](https://img.shields.io/pypi/v/grasp2alm)](https://pypi.org/project/grasp2alm/)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/grasp2alm)\n![build status](https://github.com/yusuke-takase/grasp2alm/actions/workflows/test.yml/badge.svg?branch=master)\n![PyPI - License](https://img.shields.io/pypi/l/grasp2alm)\n\nThis package supports the conversion from beam data calculated using [GRASP](https://www.ticra.com/software/grasp/) for CMB experiments to spherical harmonic coefficients ($a_{\\ell m}$) based on the [HEALPix](https://healpix.sourceforge.io/) framework.\nThe code is designed based on [Beam](https://github.com/zonca/planck-levelS/tree/master/Beam), which is part of [LevelS](https://github.com/zonca/planck-levelS), the pipleline of the Planck experiment.\n\n## Instllation\n\n```\npip install grasp2alm\n```\n\nOr you can install it from the GitHub source by:\n\n```\ngit clone https://github.com/yusuke-takase/grasp2alm\ncd grasp2alm\npip install -e .\n```\n',
    'author': 'yusuke-takase',
    'author_email': 'takase_y@s.okayama-u.ac.jp',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/yusuke-takase/grasp2alm',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.13',
}


setup(**setup_kwargs)
