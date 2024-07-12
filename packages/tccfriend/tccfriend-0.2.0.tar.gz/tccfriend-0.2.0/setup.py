from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.2.0'
DESCRIPTION = 'tccfriend package'

# Setting up
setup(
    name="tccfriend",
    version=VERSION,
    author="Nicolas Tercé",
    author_email="<nterce@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['pyqt5', 'matplotlib', 'pyrebase4'],
    keywords=['python', 'tcc', 'graph', 'french', 'application'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
