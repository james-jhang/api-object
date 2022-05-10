import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="api-object",
    version="0.0.1",
    author="Julia, Shawn, and James",
    author_email="author@example.com",
    description="OO design for Web APIs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://little-gitlab.sunbird.tw/refactoring/api-object.git",
    project_urls={
        "Bug Tracker": "http://little-gitlab.sunbird.tw/refactoring/api-object",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)