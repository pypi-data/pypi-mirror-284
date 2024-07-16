# -*- coding: UTF-8 -*-
from setuptools import setup, find_packages


def is_requirement(line):
    return not (line.strip() == "" or line.strip().startswith("#"))


with open('README.md') as readme_file:
    README = readme_file.read()

with open("requirements.txt") as f:
    REQUIREMENTS = [line.strip() for line in f if is_requirement(line)]

setup_args = dict(
    name='oarelatedworkevaluator',
    version='1.0.0',
    description='Package for evaluation of OARelatedWork dataset.',
    long_description_content_type="text/markdown",
    long_description=README,
    license='The Unlicense',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    author='Martin Dočekal',
    keywords=['dataset', 'OARelatedWork evaluation', 'OARelatedWork dataset'],
    url='https://github.com/KNOT-FIT-BUT/OARelatedWorkEvaluator',
    python_requires='>=3.10',
    install_requires=REQUIREMENTS
)

if __name__ == '__main__':
    setup(**setup_args)
