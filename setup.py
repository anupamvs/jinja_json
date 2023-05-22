from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in jinja_json/__init__.py
from jinja_json import __version__ as version

setup(
	name="jinja_json",
	version=version,
	description="json parser",
	author="anupamvs",
	author_email="hello@anupamvs.dev",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
