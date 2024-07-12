from setuptools import setup, find_packages

setup(
    name='showquota',
    version='1.0.2',
    packages=find_packages(),
    install_requires=[
        'paramiko',
    ],
    entry_points={
        'console_scripts': [
            'showquota = showquota.main:main',
        ],
    },
    author='Giulio Librando',
    author_email='giuliolibrando@gmail.com',
    description='Show user and projects storage quotas.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/giuliolibrando/showquota',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
