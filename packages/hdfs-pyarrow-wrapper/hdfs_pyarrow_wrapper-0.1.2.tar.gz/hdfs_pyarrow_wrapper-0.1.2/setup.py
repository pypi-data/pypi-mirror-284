from setuptools import setup, find_packages

setup(
    name="hdfs_pyarrow_wrapper",
    version="0.1.2",
    author="Zhang Xin",
    author_email="xinzhang.hello@gmail.com",
    description="A wrapper for the HDFS API, using pyarrow",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        # List your dependencies here
    ],
)