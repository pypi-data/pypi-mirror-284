# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['msteams_tickler']

package_data = \
{'': ['*']}

install_requires = \
['sqlmodel>=0.0.19,<0.0.20', 'typer-slim>=0.12.3,<0.13.0']

entry_points = \
{'console_scripts': ['msteams-tickler = msteams_tickler.main:main']}

setup_kwargs = {
    'name': 'msteams-tickler',
    'version': '0.1.3',
    'description': 'CLI tool for macOS to check MS Teams token expiration and send notifications',
    'long_description': '# MSTeams-Tickler\n\nMSTeams-Tickler is a command-line interface (CLI) tool that checks the expiration of Microsoft Teams tokens on macOS.\n\nCurrently only supports MS Teams classic (old version) on MacOs.\n\n\n## Installation\n\nTo install MSTeams-Tickler, you can use pip:\n\n```bash\npip install msteams-tickler\n```\n\n## Usage\nUsage\nTo use MSTeams-Tickler, you can run the main script with Python:\n\n```bash\nmsteams-tickler\n```\nBy default, MSTeams-Tickler checks the token named "authtoken" in the Teams cookies sqlite file at "~/Library/Application Support/Microsoft/Teams/Cookies". \nIf you want to check a different token or use a different cookies file, you can provide them as options:\n\n```bash\nmsteams-tickler --cookies-path /path/to/cookies --token-name other_tokenh\n```\n\n## Contributing\nIf you want to contribute to MSTeams-Tickler, feel free to open an issue or submit a pull request.  \n\n## License\n\nMSTeams-Tickler is licensed under the MIT License. See LICENSE for more information.\n',
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
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
