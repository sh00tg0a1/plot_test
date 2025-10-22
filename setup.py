from setuptools import setup, find_packages

setup(
    name="plot-test",
    version="0.1.0",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "matplotlib>=3.5.0",
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "openpyxl>=3.0.0",
        "pyarrow>=5.0.0",
        "seaborn>=0.11.0",
        "fonttools>=4.0.0",
    ],
)
