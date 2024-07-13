from setuptools import setup, find_packages

setup(
    name='siura',
    version='1.1.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'python-dotenv',
    ],
    entry_points={
        'console_scripts': [
           
        ],
    },
    author='WAMY S.A.S',
    author_email='dev@siura.com',
    description='SDK for SIURA',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/siura/sdk',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)