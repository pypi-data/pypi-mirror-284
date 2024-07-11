from setuptools import setup

name='libhupf'
version='0.11'
packages=['libhupf']
author = 'Jose Capco'
data_files = []
python_tag='py2.py3-none-win32'
dll_files = ['bin/win32/libhupf.dll']
data_files.append(('Lib/site-packages/%s' % name, dll_files))

setup(
  name=name,    
  version=version,
  packages=packages,
  python_tag = python_tag,
  package_data = {'libhupf': dll_files},
  include_package_data=True,
  author = author,
  data_files = data_files
)
