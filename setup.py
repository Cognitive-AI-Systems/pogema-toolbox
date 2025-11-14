import codecs
import os
import re

from setuptools import setup, find_packages

cur_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(cur_dir, 'README.md'), 'rb') as f:
    lines = [x.decode('utf-8') for x in f.readlines()]
    lines = ''.join([re.sub('^<.*>\n$', '', x) for x in lines])
    long_description = lines


def read(*parts):
    with codecs.open(os.path.join(cur_dir, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        version_file,
        re.M,
    )
    if version_match:
        return version_match.group(1)

    raise RuntimeError("Unable to find version string.")


setup(
    name='pogema-toolbox',
    author='Alexey Skrynnik',
    license='Apache License 2.0',
    version=find_version("pogema_toolbox", "__init__.py"),
    description='Evaluation toolbox for Pogema environment',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Tviskaron/pogema-toolbox',
    install_requires=[
        "loguru<=0.7.2",
        "matplotlib<=3.8.3",
        "seaborn~=0.13.2",
        "tabulate>=0.8.7,<=0.8.10",
        "importlib-metadata==4.13.0",
        "dask[distributed]",
        "pydantic>=1.8.2,<=1.9.1",
        "pandas<=2.2.1",
        "PyYAML<=6.0.1",
        "git+https://github.com/Cognitive-AI-Systems/pogema.git"
    ],
    extras_require={

    },
    package_dir={'': './'},
    packages=find_packages(where='./', include='pogema_toolbox*'),
    include_package_data=True,
    python_requires='>=3.8',
    package_data={
        'pogema_toolbox': ['maps/*.yaml'],
    },
)
