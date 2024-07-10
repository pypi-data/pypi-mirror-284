from setuptools import setup, find_packages

setup(
    name="stevenmeng-first-py",
    version="0.1.0",
    description="A brief description of my package",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="stevenmeng",
    author_email="stevenmeng987@gmail.com",
    url="https://github.com/yourusername/your-repo",
    packages=find_packages(),
    install_requires=[
        # List your package dependencies here
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
