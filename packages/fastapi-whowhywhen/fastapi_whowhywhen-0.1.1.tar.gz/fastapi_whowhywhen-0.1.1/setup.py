from setuptools import setup, find_packages

setup(
    name="fastapi-whowhywhen",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "httpx",
        "starlette"
    ],
    author="Mihir Khandekar",
    author_email="mihirkhandekar@gmail.com",
    description="WhoWhyWhen middleware for FastAPI",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/navig-me/fastapi-whowhywhen",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
