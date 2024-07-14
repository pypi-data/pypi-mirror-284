from setuptools import setup, find_packages

setup(
    name="forensic-doctor",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "pytsk3",
        "pyewf"
    ],
    entry_points={
        'console_scripts': [
            'forensic-doctor=forensic_doctor.forensic_doctor:main',
        ],
    },
    author="MrFidal",
    author_email="mrfidal@proton.me",
    description="A forensic tool for recovering deleted files from disk images.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Bytebreach/forensic-doctor",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
