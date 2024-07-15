#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f: # README.md 내용 읽어오기
	  long_description = f.read()

setup(
	name='CNUFOF_utils',
	version='1.0.6', 
	long_description = long_description, 
	long_description_content_type = 'text/markdown', 
	description='Parallalization Friends Of Friends based on observation data.', 
	author='Dongyun Kwak', 
	author_email='98ehddbs@naver.com', 
	url='https://github.com/dongyun-gwag', 
	license='MIT', # 라이센스 등록
	python_requires='>= 3.9.18', #파이썬 버전 등록
	install_requires=[ 'ray', 'astropy','pandas','pydl','tqdm'], # module 필요한 다른 module 등록
	packages_data={'functions':'*.py'} # 업로드할 module이 있는 폴더 입력
)

