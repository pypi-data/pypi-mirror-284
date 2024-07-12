from setuptools import setup, find_packages

setup(
    name='USAggregate',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'uszipcode',
        'us'
    ],
    author='Ethan Doshi',
    author_email='ethan.doshi@gmail.com',
    description='A package for aggregating and merging US geographic data frames.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ethand05hi/USAggregate',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)