# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

from pathlib import Path
this_directory = Path(__file__).parent
LONG_DESCRIPTION = (this_directory / "README.md").read_text()

VERSION = '1.0.9'
DESCRIPTION = 'REST API client for Fosfor AI to register models and get model details.'

setup(
    name="fosforml",
    package_dir={"fosforml":"fosforml"},
    version=VERSION,
    description=DESCRIPTION,
    url="https://gitlab.fosfor.com/fosfor-decision-cloud/intelligence/refract-sdk.git",
    author="Mahesh Gadipea",
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author_email="mahesh.gadipea@fosfor.com",
    classifiers=["Programming Language :: Python :: 3.8"],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "cloudpickle==2.2.1",
        'snowflake-ml-python==1.5.0; python_version<="3.9"',
        'snowflake-ml-python==1.5.1; python_version=="3.10"',
        'snowflake-ml-python==1.5.3; python_version>="3.11"',
        'scikit-learn==1.3.2'
    ],
    keywords=['fosforml'],
    project_urls={
        "Product": "https://www.fosfor.com/",
        "Source": "https://gitlab.fosfor.com/fosfor-decision-cloud/intelligence/refract-sdk/-/tree/main/fosforml?ref_type=heads",
    }
)
 
