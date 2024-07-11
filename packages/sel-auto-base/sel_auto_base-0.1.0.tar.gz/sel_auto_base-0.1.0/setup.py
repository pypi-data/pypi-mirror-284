# setup.py

from setuptools import setup, find_packages

setup(
    name='sel_auto_base',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'selenium',
    ],
    author='QAR-LEAF PRIVATE LIMITED',
    author_email='support@qarleaf.com',
    description='A basic Selenium wrapper for Python',
    # url='',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
