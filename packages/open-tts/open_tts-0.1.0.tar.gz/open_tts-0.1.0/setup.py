from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="open-tts",
    version="0.1.0",
    author="sandesh kumar",
    author_email="support@sandeshai.in",
    description="A Python module for text-to-speech conversion using an open API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sandeshaiplus/open-tts",
    packages=find_packages(),
    install_requires=[
        "requests",
        "playsound",
        "colorama",
        "beautifulsoup4",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires='>=3.6',
)