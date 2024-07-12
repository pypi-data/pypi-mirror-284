from setuptools import setup, find_packages

setup(
    name='showquota',
    version='1.0.0',
    packages=find_packages(),
    scripts=['showquota/main.py'],
    entry_points={
        'console_scripts': [
            'showquota = showquota.showquota:main',
        ],
    },
    install_requires=[
        'paramiko',
    ],
    package_data={
        '': ['config.cfg'],  
    },
    include_package_data=True,
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
