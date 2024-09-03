from setuptools import setup, find_packages

setup(
    name='CalculatorAli',
    version='3.0',
    packages=find_packages(),
    py_modules=['CalculatorAli'],
    install_requires=[
        'CaclUi',
    ],
        author='Muhammad Ali Asghar',
        author_email='ali.asghar@brightnexus.com',
        description='Performs basic calculation operations',
        entry_points={
                'console_scripts': [
                        'CalculatorAli=pythonProject:CalculatorAli',  # Updated to reflect the new import path
                ],
        },
)
