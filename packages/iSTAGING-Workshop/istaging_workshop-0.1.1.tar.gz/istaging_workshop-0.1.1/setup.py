from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="iSTAGING_Workshop",
    description="Example package for the iSTAGING Workshop",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="0.1.1",
    author="George Aidinis",
    author_email="George.Aidinis@Pennmedicine.upenn.edu",
    maintainer="George Aidinis",
    maintainer_email="George.Aidinis@pennmedicine.upenn.edu",
    url="https://github.com/georgeaidinis/iSTAGING_Workshop",
    download_url="https://github.com/georgeaidinis/iSTAGING_Workshop/archive/refs/tags/v0.1.zip",
    project_urls={
        "Bug Tracker": "https://github.com/georgeaidinis/iSTAGING_workshop/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Healthcare Industry",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    keywords = [
                    'medical image analysis',
                ], 
    packages=find_packages(exclude=["tests", ".git"]),
    python_requires=">=3.8",
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn",
        "spare-scores",
    ],
    tests_require=[
        "pytest",
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': ['iSTAGING_Workshop=cli:main']
        },
)