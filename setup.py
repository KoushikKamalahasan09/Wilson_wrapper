from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()


setup(
    name="wilson_Beta_wrapper",                  # pip install wilson_Beta_wrapper
    version="0.1.0",
    author="Koushik Kamalahasan",
    author_email="koushikkamalahasan@gmail.com",
    description="A wrapper to modify beta functions in the Wilson SMEFT package.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),              # Automatically finds 'wilson_wrapper'
    python_requires=">=3.7",
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Or your license
        "Operating System :: OS Independent",
    ],
)