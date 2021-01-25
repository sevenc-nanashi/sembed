import setuptools

with open("README.md", "r", encoding='utf-8') as f:
    long_desc = f.read()


def _requires_from_file(filename):
    return open(filename, encoding="utf8").read().splitlines()


setuptools.setup(
    name="sembed",
    version="1.0.5",
    author="sevenc_nanashi",
    description="A wrapper of discord.Embed.",
    long_description=long_desc,
    long_description_content_type='text/markdown',
    url="https://github.com/sevenc-nanashi/sembed",
    packages=setuptools.find_packages(),
    install_requires=_requires_from_file('requirements.txt'),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
