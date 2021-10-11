"""Setup.py for DB2 custom Airflow provider package."""

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

"""Perform the package airflow-provider-DB2-custom setup."""
setup(
    name='airflow-provider-db2-custom',
    version="0.0.1",
    description='A provider package built by AIOPS IBM team',
    long_description=long_description,
    long_description_content_type='text/markdown',
    entry_points={
    "apache_airflow_provider": [
        "provider_info=db2_provider.__init__:get_provider_info"
          ]
      },
    license='Apache License 2.0',
    packages=['db2_provider', 'db2_provider.hooks'],
    install_requires=['apache-airflow>=2.0'],
    setup_requires=['setuptools', 'wheel'],
    author='Fernanda Milagres',
    author_email='fernanda.milagres@ibm.com',
    python_requires='~=3.7',
)