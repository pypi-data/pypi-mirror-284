# setup.py
from setuptools import setup, find_packages

setup(
    name='xbrlapi',
    version='0.1.2',  # Increment the version number
    packages=find_packages(),
    install_requires=[
        'requests',
        'supabase',
    ],
    entry_points={
        'console_scripts': [
            # Define any scripts here if needed
        ],
    },
)
