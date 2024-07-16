from setuptools import setup, find_packages

setup(
    name='CLI_EXPORTER',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'pandas',
        'python-docx',
    ],
    entry_points='''
        [console_scripts]
        myapp=my_application.cli:cli
    ''',
    author='Rachmann Joubert',
    description='CLI application to automate data extraction and formating for Bitwarden csv import',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
