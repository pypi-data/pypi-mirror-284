# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['msteams_tickler', 'msteams_tickler.classic']

package_data = \
{'': ['*']}

install_requires = \
['binary-cookies-parser>=0.1.3,<0.2.0',
 'pytz>=2024.1,<2025.0',
 'sqlmodel>=0.0.19,<0.0.20',
 'typer-slim>=0.12.3,<0.13.0']

entry_points = \
{'console_scripts': ['mstc = msteams_tickler.main:main']}

setup_kwargs = {
    'name': 'msteams-tickler',
    'version': '1.0.1',
    'description': 'CLI tool for macOS to check MS Teams token expiration and send notifications',
    'long_description': '# MSTeams-Tickler\n\nMSTeams-Tickler is a command-line interface (CLI) tool that checks the expiration of Microsoft Teams tokens on macOS.\n\n\n## Installation\n\nTo install MSTeams-Tickler, you can use pip:\n\n```bash\npip install msteams-tickler\n```\n\n## Usage\nUsage\n\nTo use MSTeams-Tickler, run:\n\n```bash\nmstc check\n```\n\nor for MSTeams classic \n```bash\nmstc classic check\n```\n\nMSTeams uses a binarycookies file to store the tokens.  MSTeams-Tickler looks for the binarycookies file at the default location.\nIf you have the binarycookies file at a different location, you can specify the path to the binarycookies file using the `--cookies-path` option:\n\n```bash\nmstc check --cookies-path /path/to/cookies.binarycookies --token-name other_token\n```\n! MSTeams classic looks for a sqlite file at the default cookies location.  If you have the sqlite file at a different location,\nyou can specify the path to the sqlite file using the `--cookies-path` option:\n\n## Contributing\nIf you want to contribute to MSTeams-Tickler, feel free to open an issue or submit a pull request.  \n\n## License\n\nMSTeams-Tickler is licensed under the MIT License. See LICENSE for more information.\n',
    'author': 'Daniel Tom',
    'author_email': 'daniel.tom@xebia.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
