import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "python_api_current_temperature",
    version = "0.0.1",
    author = "AmirHossein Amirzadeh",
    author_email = "Amirzadeh@live.com",
    description = "A simple client module to get temperature from different service providers over api",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/AmirhosseinAmirzadeh/Python-Current-Temp-Api",
    project_urls = {
        "Author": "https://eamirzadeh.ir",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = [
        'requests',
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.6"
)