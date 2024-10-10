from setuptools import setup, find_packages

setup(
    name="dummy-package",
    version="0.1.0",
    packages=find_packages(),
    description="A dummy package for demonstration purposes",
    author="Priyanshu Jangir",
    author_email="priyanshu.jangir@elastiq.ai",
    url="https://github.com/priyanshu-jangir-elastiq/dummy-package",  # Update with your GitHub repo link
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)