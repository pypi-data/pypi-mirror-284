from setuptools import setup, find_packages

VERSION:str = "0.0.1.dev01"
DESCRIPTION:str = "Wame Game Engine"
LONG_DESCRIPTION:str = "Pygame Wrapper to Make Creating and Managing Games Easier"

setup(
    name="wame-engine",
    version=VERSION,
    author="WilDev Studios",
    author_email="support@wildevstudios.net",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["pygame"],
    keywords=["python", "pygame", "wrapper", "engine", "game"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Games/Entertainment",
        "Topic :: Software Development :: Libraries :: pygame"
    ]
)