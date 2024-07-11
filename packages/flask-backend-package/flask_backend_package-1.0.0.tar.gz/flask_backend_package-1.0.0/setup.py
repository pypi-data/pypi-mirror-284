from setuptools import setup, find_packages

setup(
    name="flask_backend_package",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "Flask>=3.0.3",
        "blinker>=1.8.2",
        "certifi>=2024.7.4",
        "charset-normalizer>=3.3.2",
        "click>=8.1.7",
        "colorama>=0.4.6",
        "dnspython>=2.6.1",
        "Flask-PyMongo>=2.3.0",
        "idna>=3.7",
        "importlib_metadata>=8.0.0",
        "itsdangerous>=2.2.0",
        "Jinja2>=3.1.4",
        "MarkupSafe>=2.1.5",
        "pymongo>=4.8.0",
        "requests==2.32.3",
        "urllib3==2.2.2",
        "Werkzeug>=3.0.3",
        "zipp>=3.19.2"
    ],
)
