import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lazyscience",  # Replace with your own username
    version="0.0.2",
    author="Shinya Ito",
    author_email="shixnya@gmail.com",
    description="A bunch wrappers for lazy scientists",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shixnya/lazyscience",
    project_urls={
        "Bug Tracker": "https://github.com/shixnya/lazyscience/issues",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=["numpy", "scipy", "h5py", "iminuit"],
)
