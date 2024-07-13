from setuptools import setup, find_packages

setup(
    name="mysimplepackage_wl2901",
    version="0.2",
    packages=find_packages(),
    include_package_data=True,
    description="A simple example package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/mysimplepackage",
    author="Your Name",
    author_email="yourname@example.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
