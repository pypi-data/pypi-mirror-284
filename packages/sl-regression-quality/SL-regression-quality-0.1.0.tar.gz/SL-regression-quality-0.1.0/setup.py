from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup (
    name='SL-regression-quality',
    version='0.1.0',
    license='MIT',
    description='simple linear regression quality',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author= 'EdelH, Aplata',
    packages=find_packages(),
    install_requires = ['numpy','pandas','statsmodels','scikit-learn','art'],

    url='https://github.com/aplatag/project_SL_regression_quality.git'
)
