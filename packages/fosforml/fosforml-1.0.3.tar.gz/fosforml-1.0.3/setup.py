# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

from pathlib import Path
this_directory = Path(__file__).parent
LONG_DESCRIPTION = (this_directory / "README.md").read_text()

VERSION = '1.0.3'
DESCRIPTION = 'REST API client for Fosfor AI to register models and get model details.'

setup(
    name="fosforml",
    package_dir={"fosforml":"fosforml"},
    version=VERSION,
    description=DESCRIPTION,
    url="https://gitlab.fosfor.com/fosfor-decision-cloud/intelligence/refract-sdk.git",
    author="Rakesh Gadiparthi",
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author_email="rakesh.gadiparthi@fosfor.com",
    classifiers=["Programming Language :: Python :: 3.8"],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "cloudpickle==2.2.1",
        "requests-toolbelt==1.0.0",
        "shutils==0.1.0",
        "PyYAML==6.0.1",
        "mosaic-utils",
        "urllib3==2.2.1",
        'numpy==1.26.4; python_version>"3.8"',
        'numpy==1.24.4; python_version<="3.8"',
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
 
