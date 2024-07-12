from setuptools import setup, find_packages

setup(
    name='dname_code',
    version='1.1',
    packages=find_packages(),
    install_requires=[
        # Add dependencies here.
        # e.g. 'numpy>=1.11.1'
    ],
    entry_points={
        "console_scripts": [
            "dname-code = dname_code:hello"
        ],
    },
    # author='Daris',
    # author_email='hei.raymond.2@gmail.com',
    # description='A simple Python package',
    # url='https://github.com/dnamecode/simple-python-package',
)