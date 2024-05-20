# -*- coding: utf-8 -*-
"""
Created on Fri May 17 17:11:21 2024

@author: jcp
"""

import setuptools

# Define the project metadata
name = 'font_path'
version = '1.0'
author = 'Park Juchan'
author_email = 'pjc6269@gmail.com'
description = 'Automatically finds font paths using os.getlogin() and fm.fontManager'
url = 'https://github.com/chance6269/modules'  # Replace with your project URL
license = 'MIT'

# Define dependencies
requires = [
    'matplotlib.font_manager',
    'os'
]

# Define package contents
packages = [
    'add_font',
]

# Define entry points (if any)
entry_points = {}

# Set up the package
setuptools.setup(
    name=name,
    version=version,
    author=author,
    author_email=author_email,
    description=description,
    url=url,
    license=license,
    requires=requires,
    packages=packages,
    entry_points=entry_points
)
