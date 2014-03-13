try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="nfbsearch-flask",
    author="Hugo Bastien",
    author_email="hugobast@gmail.com",
    url="",
    version="0.0.1",
    packages=[
        "nfbsearch_flask"
    ],
    tests_require=[
        "mock",
        "nose",
        "nosepride"
    ],
    install_requires=[
        "flask",
        "elasticsearch",
        "nose",
        "setuptools"
    ],
    test_suite='tests',
    license="",
    description="",
    long_description=""
)