import setuptools

with open("README.md", "r",encoding="utf-8") as fh:
    long_description = fh.read()

with open('requirements.txt',encoding="utf-8") as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="wea-display-schema",
    version="1.0.0",
    #use_scm_version=True,
    setup_requires=['setuptools_scm'],
    author="wea Tools",
    author_email="info@wea.tools",
    description="wea-display Data-Model Objects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wea-tools/wea-display-schema",
    packages=setuptools.find_packages(exclude=["tests", "scripts", "samples"]),
    install_requires=requirements,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Operating System :: OS Independent"
    ],
)
