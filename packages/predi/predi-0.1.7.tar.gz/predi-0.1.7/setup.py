from setuptools import setup, find_packages

setup(
    name='predi',  # Lowercase package name to ensure consistency
    version='0.1.7',
    author='Mojtaba Eshghie',
    author_email='eshghie@kth.se',
    description='PreDi: Symbolic Solidity Predicate Difference Tool',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mojtaba-eshghie/PreDi',
    packages=find_packages(where='src'),  # Find packages in the 'src' directory
    package_dir={'': 'src'},  # Define the package directory
    install_requires=[
        'sympy>=1.13.0rc2',
        'colorama>=0.4.6',
        'pyyaml>=6.0.1'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
