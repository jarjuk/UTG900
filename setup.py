import setuptools

with open("VERSION", "r") as fh:
    version = fh.read().rstrip()

scripts =[ ]
name="utg900"

print( "version", version, ", packages", setuptools.find_packages())
    
setuptools.setup(
    name=name, # Replace with your own username
    version=version,
    author="jj",
    author_email="author@example.com",
    description="UTG-900 - Tool to control UNIT-T UTG900 Waveform generator",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    package_data={
        "UTG900": ['../VERSION', '../RELEASES.md' ]
    },
    scripts=scripts,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
