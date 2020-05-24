from setuptools import setup, find_packages

setup(
    name="homework",
    packages=find_packages(where='src'),
    include_package_data=True,
    package_dir={'': 'src'},
)
