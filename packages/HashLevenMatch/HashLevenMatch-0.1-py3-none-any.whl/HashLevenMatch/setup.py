from setuptools import setup

setup(
    name='HashLevenMatch',                   
    version='0.1',                           
    description='Library to utilize inexact matching.',  
    packages=['HashLevenMatch'],             
    author_email='davislspradling@gmail.com',
    zip_safe=False,
    install_requires=[
        'python-Levenshtein',
        'csv',
        'matplotlib',
        'pandas',
        'numpy'
    ]
)
