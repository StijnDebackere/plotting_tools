import setuptools

setuptools.setup(
    name="plotting_tools",
    version="0.0.1",
    author="Stijn Debackere",
    author_email="debackere@strw.leidenuniv.nl",
    description="Tools to bend matplotlib to my will.",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    url="https://github.com/StijnDebackere/plotting_tools",
    packages=['plotting_tools'],
    install_requires=[
        "matplotlib",
        "numpy",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
