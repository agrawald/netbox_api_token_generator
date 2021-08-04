from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='netbox_api_token_generator',
    version='0.1',
    description='NetBox plugin to generate API token for a user',
    url='https://github.com/agrawald/netbox_api_token_generator.git',
    author='Dheeraj Agrawal',
    author_email='agrawal.dheeraj.7@gmail.com',
    license='Apache 2.0',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[],
    packages=["netbox_api_token_generator", "netbox_api_token_generator.api"],
    include_package_data=True,
    zip_safe=False,
)