from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

VERSION = '0.1.8'
DESCRIPTION = 'Chain Logger to distinct each request for Python Web Server (Support Flask and FastAPI) and looks like the logger is chained'

# Setting up
setup(
    name="chain-logging",
    version=VERSION,
    author="danangjoyoo (Agus Danangjoyo)",
    author_email="<agus.danangjoyo.blog@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['fastapi', 'logging'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Environment :: Web Environment",
        "Operating System :: OS Independent",
        "Typing :: Typed"
    ],
    url="https://github.com/Danangjoyoo/chain-logging"
)
