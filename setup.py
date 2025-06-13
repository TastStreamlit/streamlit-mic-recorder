from pathlib import Path

import setuptools

this_directory = Path(__file__).parent

setuptools.setup(
    name="streamlit_mic_recorder",
    version="0.0.8",
    author="Baptiste Ferrand",
    author_email="bferrand.math@gmail.com",
    description="Streamlit component that allows to record mono audio from the user's microphone, and/or perform speech recognition directly.",
    url="https://github.com/B4PT0R/streamlit-mic-recorder",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.7",
    install_requires=[
        "streamlit >= 0.63",
        "SpeechRecognition"
    ],
)
