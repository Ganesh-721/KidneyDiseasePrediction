import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

__version__ = '0.1.0'

repo_name = "KidneyDiseasePrediction"
author_name = "Ganesh-721"
author_email = "saiganeshpaindla99@gmail.com"
SRC_REPO = "cnnClassifier"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=author_name,
    author_email=author_email,
    description="A small example package",
    long_description=long_description,
   _description_content_type="text/markdown",
    url=f"https://github.com/{author_name}/{repo_name}",
    project_urls={
        "Bug Tracker": f"https://github.com/{author_name}/{repo_name}/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
)