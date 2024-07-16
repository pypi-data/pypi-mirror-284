from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='omip',  # required
    version='2024.7.15',
    description='omip: utilities for processing OMIP data',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Feng Zhu',
    author_email='fengzhu@ucar.edu',
    url='https://github.com/fzhu2e/omip',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    zip_safe=False,
    keywords='Ocean Model Intercomparison Project',
    classifiers=[
        'Natural Language :: English',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    install_requires=[
        'netCDF4',
        'xarray',
        'dask',
        'nc-time-axis',
        'colorama',
        'tqdm',
    ],
)
