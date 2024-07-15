from setuptools import setup, find_packages

setup(
    name="dfa-gen",
    version="0.1",
    description='Python package for generating mRNA DFA from protein sequence and visualizing it as a graph image',
    packages=find_packages(),
    install_requires=[
        "pandas",
        "graphviz"
    ],
    entry_points={
        "console_scripts": [
            "dfa-gen=dfa_gen.generate_dfa:main",
        ],
    },
)
