from setuptools import setup, find_packages

setup(
    name='digitalsigtool',
    version='0.1.0',
    description='A tool to generate and verify digital signatures for files using SHA-256 and a secret key.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Babar Ali Jamali',
    author_email='babar995@gmail.com',
    url='https://github.com/babaralijamali/digitalsigtool',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'digitalsigtool=digitalsigtool.digitalsigtool:main',
        ],
    },
)
