from setuptools import setup

with open(file="README.md", mode="r", encoding="utf8") as fh:
    long_description = fh.read()

setup(
    name='aditya',
    version='0.1',
    author="Aditya Raj",
    author_email="adityaraj867604@gmail.com",
    description='My personal tools',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/ed21b006/',  # Adjust as necessary
    py_modules=['streaming_stats'],
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
)