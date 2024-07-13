import setuptools

setuptools.setup(
    name = "pywebviewcv",
    version = "2",
    author = "qaqFei",
    author_email = "qaq_fei@163.com",
    description = "A Canvas based webview for Python",
    long_description = open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type = "text/markdown",
    url = "https://github.com/qaqFei/pywebviewcv",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires = ">=3.12.0",
)