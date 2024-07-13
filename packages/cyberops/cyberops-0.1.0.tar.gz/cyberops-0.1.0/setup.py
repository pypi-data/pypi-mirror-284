from setuptools import setup, find_packages

setup(
    name="cyberops",
    version="0.1.0",
    author="Krishna Gopal Jha",
    author_email="krishnagopaljhaa@gmail.com",
    description="CyberOPS is a Python package for performing multiple tasks",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/cyberops",
    packages=find_packages(),
    classifiers=[
    "Development Status :: 3 - Alpha",
    ],
    python_requires='>=3.6',
)
