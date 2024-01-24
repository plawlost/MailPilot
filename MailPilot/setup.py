from setuptools import setup, find_packages
import os

def read(file_name):
    """Utility function to read the README file. Used for the long_description."""
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()

# Package meta-data.
NAME = 'MailPilot'
DESCRIPTION = 'A versatile email sending tool for personalized mass mailing.'
URL = 'https://github.com/plawlost/MailPilot'
EMAIL = 'contact@plawlost.com'
AUTHOR = "Yağız Erkam '@plawlost' Çelebi"
REQUIRES_PYTHON = '>=3.6.0'
VERSION = '1.0.0'

REQUIRED = [
    # No third-party packages required, thus the list is empty for now.
]

CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Build Tools",
    "License :: OSI Approved :: Apache Software License",
    "Programming Language :: Python :: 3",
    "Intended Audience :: Information Technology",
    "Natural Language :: English",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Operating System :: OS Independent",
    "Topic :: Communications",
    "Topic :: Communications :: Email",
    "Topic :: Communications :: Email :: Mail Transfer Agents (MTA)",
    "Topic :: Communications :: Email :: Mailing List Administration",
    "Topic :: Communications :: Email :: News",
    "Topic :: Communications :: Email :: News :: Front-Ends",
    "Topic :: Communications :: Email :: News :: Posting",
]

# Where the magic happens:
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    install_requires=REQUIRED,
    include_package_data=True,
    license='Apache License 2.0',
    classifiers=CLASSIFIERS,
    # Additional metadata to consider for additional entries:
    # package_data={"mailpilot": ["templates/*.html", "config/*.ini"]},
    # data_files=[('config', ['mailpilot/config/mailpilot_config.ini'])],
    # Possible CLI scripts
    entry_points={
        'console_scripts': [
            'mailpilot=mailpilot.__main__:main',
        ],
    },
)