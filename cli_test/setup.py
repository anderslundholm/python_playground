from setuptools import setup, find_packages


setup(
    name='cli_test',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        cli=click_cli.cli:cli
    ''',
)