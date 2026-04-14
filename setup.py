from setuptools import setup, find_packages

setup(
    name='rl_trading_bot',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[],
    author='Jay',
    description='A production-ready ML pipeline',
)
