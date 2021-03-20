import setuptools
from sembed import __version__

with open("README.md", "r", encoding='utf-8') as f:
    long_desc = f.read()


def _requires_from_file(filename):
    return open(filename, encoding="utf8").read().splitlines()


setuptools.setup(
    name="sembed",
    version=__version__,
    author="sevenc_nanashi",
    description="A wrapper of discord.Embed.",
    long_description=long_desc,
    long_description_content_type='text/markdown',
    url="https://github.com/sevenc-nanashi/sembed",
    packages=['discord.ext.sembed', 'sembed'],
    project_urls={
        "Bug Tracker": "https://github.com/sevenc-nanashi/sembed/issues",
    },
    install_requires=_requires_from_file('requirements.txt'),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
