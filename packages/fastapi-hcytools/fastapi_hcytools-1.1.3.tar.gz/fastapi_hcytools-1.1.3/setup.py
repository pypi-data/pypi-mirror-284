from setuptools import setup, find_packages
import fastapi_hcytools

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='fastapi-hcytools',
    version=fastapi_hcytools.__version__,
    description='fastapi start tool',
    author='yang-haechan',
    author_email='gocks4560@gmail.com',
    url='https://github.com/yang-haechan/fastapi_start',
    install_requires=requirements,
    packages=find_packages(),
    keywords=['yang-haechan', 'hcytools'],
    python_requires='>=3.11',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.11',
	    'Programming Language :: Python :: 3.12',
    ],
)