from setuptools import setup, find_packages
import os
import shutil
import sys

def copy_app_files():
    package_path = os.path.dirname(os.path.abspath(__file__))
    app_name = 'referrals'
    app_source_path = os.path.join(package_path, app_name)
    app_dest_path = os.path.join(package_path, app_name)

    if os.path.exists(app_source_path):
        for item in os.listdir(app_source_path):
            source = os.path.join(app_source_path, item)
            destination = os.path.join(app_dest_path, item)
            if os.path.isdir(source):
                shutil.copytree(source, destination)
            else:
                shutil.copy2(source, destination)

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="django-baboons-referral",
    version="0.1.8", 
    author="Wilbur Hachita",
    author_email="wilbur@baboons.nl",
    description="A reusable Django app for managing user referrals.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/willbur-hachita/django-referral",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "Django>=3.2",
        "djangorestframework",
    ],
)

if 'install' in sys.argv or 'develop' in sys.argv:
    copy_app_files()
