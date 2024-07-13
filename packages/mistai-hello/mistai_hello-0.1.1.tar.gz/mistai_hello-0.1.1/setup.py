from setuptools import setup, find_packages

VERSION = "0.1.1"
DESCRIPTION = 'PyPi Template for mist.ai'
LONG_DESCRIPTION = 'A PyPi package from mist.ai that can be used as a template. Code can be found on GitHub.'

# Setting up
setup(
    name="mistai-hello",
    version=VERSION,
    author="Team mist.ai",
    author_email="sandev.20@cse.mrt.ac.lk",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'mist.ai', 'template'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)