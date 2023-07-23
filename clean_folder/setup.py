from setuptools import setup, find_packages

setup(
    name='clean_folder',
    version='1.0.0',
    author='Andrii Rohovyk',
    description='A Python package to clean a folder',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'clean-folder = clean_folder.clean:main'
        ]
    },
)