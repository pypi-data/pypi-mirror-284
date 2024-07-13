from setuptools import setup, find_packages

setup(
    name='osop',
    version='0.4',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'osop=osop.main:main',
        ],
    },
    include_package_data=True,
    package_data={
        '': [],
    },
)
