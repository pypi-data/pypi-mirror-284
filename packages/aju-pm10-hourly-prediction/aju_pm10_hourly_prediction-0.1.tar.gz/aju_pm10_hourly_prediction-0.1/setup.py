# setup.py
from setuptools import setup, find_packages

setup(
    name='aju_pm10_hourly_prediction',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'matplotlib',
        'seaborn',
        'scikit-learn',
        'keras'
    ],
    author='Aju Peter',
    author_email='ajupeter.t@gmail.com',
    description='A package for PM10 hourly prediction from data cleaning to prediction',
    url='https://github.com/ajupeter23/pm10_hourly_predictor',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
