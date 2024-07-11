from setuptools import setup, find_packages

setup(
    name="cvss_converter",
    version="0.1.4",
    author="SECTA5",
    author_email="hidden@secta5.com",
    description="A package to convert CVSSv2 to CVSSv3",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SECTA5/cvss-converter",
    packages=find_packages(),
    install_requires=["cvss"],
    extras_require={
        "dev": ["pytest"],  # Add pytest as an extra requirement for development
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
