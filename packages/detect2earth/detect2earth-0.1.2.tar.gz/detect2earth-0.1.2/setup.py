from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="detect2earth",
    version="0.1.2",
    author="Nur Arif",
    author_email="nurarif0151@gmail.com",
    description="This package will get the latest earthquake data from BMKG | Badan Meteorologi, Klimatologi, dan Geofisika",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ArN-1/Indonesian-earthquake-monitoring",
    project_urls={
        "Website": "https://nurarif.com"
    },
    packages=find_packages(),
    install_requires=[
        'detect2earth',

    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
