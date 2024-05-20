# -*- coding: utf-8 -*-
"""
Created on Fri May 17 17:11:21 2024

@author: jcp
"""

from setuptools import setup, find_packages



# Define the project metadata
name = 'font_path'
version = '1.0'
author = 'Park Juchan'
author_email = 'pjc6269@gmail.com'
description = 'Automatically finds font paths using os.getlogin() and fm.fontManager'
url = 'https://github.com/chance6269/font_path.git'  # Replace with your project URL


# Define dependencies
requires = [
    'matplotlib.font_manager',
    'os'
]

setup(
    name='font_path',  # 패키지 이름
    version='0.1',  # 버전
    packages=find_packages(),  # 패키지를 찾는 방법
    install_requires=requires,  # 의존성 패키지 목록
    author=name,  # 작성자 이름
    author_email=author_email,  # 작성자 이메일
    description=description,  # 패키지 설명
    long_description='A longer description of your package',  # 상세한 패키지 설명
    url=url,  # 패키지의 GitHub 저장소 URL
    license='MIT',  # 라이선스
)
