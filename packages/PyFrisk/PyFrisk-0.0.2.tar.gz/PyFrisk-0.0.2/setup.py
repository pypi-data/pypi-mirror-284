from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='PyFrisk',
  version='0.0.2',
  author='akaruineko',
  author_email='brightcat1950@gmail.com',
  description='This is the simplest module for quick work with proxy.',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/BrightCat14/Pfrisk',
  packages=find_packages(),
  install_requires=[
    'requests',
    'lxml'
  ],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='proxy ips helping',
  project_urls={
    'GitHub': 'https://github.com/BrightCat14/Pfrisk'
  },
  python_requires='>=3.6'
)