from setuptools import setup, find_packages

setup(
    name="cds_xmatch_client",
    version="0.1",
    packages=find_packages(),
    author="Ernesto Castillo N.",
    scripts=["scripts/cdsxmatch"],
    package_data = { 'cds_xmatch_client' : [ 'data/catalog_alias.json' ] }
)
