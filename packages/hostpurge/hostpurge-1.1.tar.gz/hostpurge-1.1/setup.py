from setuptools import setup, find_packages

setup(
    name='hostpurge',
    version='1.1',
    packages=find_packages(),
    install_requires=[
        # Add other dependencies here if needed
    ],
    entry_points={
        'console_scripts': [
            'hostpurge = hostpurge.hostpurge:main',
        ],
    },
    author='Hao Luo',
    author_email='luohao@caas.cn',
    description='A tool for purging host sequences from metagenomic reads',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/HaoLuo-leo/hostpurge',
    license='MIT',
)
