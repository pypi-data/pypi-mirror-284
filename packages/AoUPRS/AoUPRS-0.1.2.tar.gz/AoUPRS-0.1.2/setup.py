from setuptools import setup, find_packages

# Read the contents of the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='AoUPRS',
    version='0.1.2',  # Increment the version number
    description='AoUPRS is a Python module for calculating Polygenic Risk Scores (PRS) specific to the All of Us study',
    author='Ahmed Khattab',
    author_email='',
    url='https://github.com/AhmedMKhattab/AoUPRS',
    packages=find_packages(),
    install_requires=[
        'hail',
        'gcsfs',
        'pandas',
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
