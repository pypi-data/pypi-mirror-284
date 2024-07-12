from setuptools import setup, find_packages

setup(
    name='algocomp',
    version='1.0.2',
    packages=find_packages(include=['algocomp', 'algocomp.*']),
    install_requires=[
        'numpy',
        'matplotlib',
        'scipy',
    ],
    include_package_data=True,
    description='A package for algorithmic competition simulations.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
