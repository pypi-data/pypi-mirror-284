import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Lecaps",
    version="1.0.0",
    author="Emiliano Ezequiel",
    description="Cotizar tasas implícitas de Lecaps",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EmilianoEzequielG/Lecaps",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
