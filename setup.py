from setuptools import setup, find_packages

setup(
    name="cds_xmatch_client",
    version="0.1",
    packages=find_packages(),
    author="Ernesto Castillo N.",
    scripts=["scripts/cdsxmatch"],
    install_requires=[
     "requests >= 2.20",
     "pandas >=1.0",
     "astropy >= 3.2"
    ],
    package_data = { 'cds_xmatch_client' : [ 'data/catalog_alias.json' ] }
)
