from setuptools import setup, find_packages

setup(
    name="recogaud",
    version="0.2",
    packages=find_packages(),
    install_requires=[
        "SpeechRecognition",
        "g4f",
    ],
    author="Your Name",
    author_email="firi8228@gmail.com",
    description="A library for audio recognition and text correction",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)