from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in kpi/__init__.py
from kpi import __version__ as version

setup(
	name="kpi",
	version=version,
	description="kpi management",
	author="Lubna Hameed",
	author_email="x@example.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
