from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()

setup(
  name='ahuella',
  version='0.0.2',
  author='tembz&tenkawaa',
  author_email='tembz@vk.com',
  description='module for api.hella.team',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/tembz/ahuella',
  packages=find_packages(),
  install_requires=['aiphttp', 'dacite'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='ahuella',
  python_requires='>=3.10'
)