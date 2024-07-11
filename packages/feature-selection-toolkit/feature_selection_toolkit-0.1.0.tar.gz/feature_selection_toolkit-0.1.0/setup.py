import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="feature-selection-toolkit",
    version="0.1.0",
    author="Mevlüt Başaran",
    author_email="mevlutbasaran01@gmail.com",
    description="A comprehensive toolkit for feature selection using various statistical and machine learning methods.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mevlt01001/FutureSeleciton",
    project_urls={
        "Bug Tracker": "https://github.com/mevlt01001/FutureSeleciton/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn",
        "tqdm",
        "joblib",
        "matplotlib",
        "statsmodels",
    ],
    extras_require={
        "testing": ["pytest"],
    },
)

