from setuptools import setup, find_packages

setup(
    name="transkription_vosk",
    version="0.1.2",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "transkription_vosk=transkription_vosk.transkription_vosk:main",
        ],
    },
    install_requires=[
        "vosk",
        "pydub",
    ],
    author="Martial Job",
    author_email="transkription_vosk@mjob.me",
    description="Ein Paket zur Transkription von Audiodateien mit Vosk-Modellen, lokal auf dem Rechner.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/martialjob/transkription_vosk",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)