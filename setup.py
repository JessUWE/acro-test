from setuptools import setup, find_packages


exec(open('acro/version.py').read())

setup(
    name="acro",
    version=__version__,
    description="Tools for the Semi-Automatic Checking of Research Outputs",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "pandas>=1.5.0",
        "numpy>=1.21.0",
        "statsmodels>=0.13.0",
        "openpyxl>=3.0.0",
        "pyyaml>=5.4.0",
    ],
    extras_require={
        "doc": [
            "sphinx>=4.0.0",
            "numpydoc",
            "sphinx-autopackagesummary",
            "sphinx-issues",
            "sphinx-prompt", 
            "pydata-sphinx-theme",
            "sphinx-design",
        ]
    },
)
