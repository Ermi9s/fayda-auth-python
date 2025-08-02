from setuptools import setup, find_packages

setup(
    name="fayda_auth",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "redis==4.5.4",
        "python-dotenv==1.0.0",
        "pyjwt==2.6.0",
        "cryptography==41.0.3",
        "requests==2.31.0",
        "validator-collection==1.5.0",
        "setuptools==78.1.0",
        "jwcrypto>=1.5.0"
    ],
    author="Awura Computing PLC",
    author_email="@awuraplc.org",
    description="A python library package for Fayda Esignet authentication",
    url="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)