from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
from setuptools.command.install import install
from sys import maxsize
from os import path, listdir

BASEPATH = path.dirname(path.abspath(__file__))

class PostInstall(install):
  def run(self):
    install.run(self)
    target = path.join(BASEPATH, 'license.txt')
    self.copy_file(target, path.join(self.install_lib,'libhupf'))
    #target = path.join(self.install_lib,'libhupf')
    #self.move_file(

def rem_opt(l,keys):
  return [y for y in l if y not in keys]
  
class BuildExt(build_ext):
  def build_extensions(self):
    keys = ["-Wstrict-prototypes","-fwrapv","-g","-O1","-O2","-fstack-protector-strong","-fno-strict-aliasing"]
    self.compiler.compiler_so = rem_opt(self.compiler.compiler_so,keys)
    build_ext.build_extensions(self)
    build_path = path.abspath(self.build_temp)

if maxsize > 2**32:
  extra_compile_args = ['-DNDEBUG', '-DLIBHUPF_EXPORTS', '-O3', '-g', '-s', '-Wall', '-Wextra', '-m64', '-Wno-unknown-pragmas', '-Wno-deprecated-declarations', '-Wno-parentheses', '-Wno-unused-function', '-fopenmp', '-std=c++11', '-fpic']
else:
  extra_compile_args = ['-DNDEBUG', '-DLIBHUPF_EXPORTS', '-O3', '-g', '-s', '-Wall', '-Wextra', '-m32', '-Wno-unknown-pragmas', '-Wno-deprecated-declarations', '-Wno-parentheses', '-Wno-unused-function', '-fopenmp', '-std=c++11']
      
module = Extension('libhupf.libhupf',
  sources = ['libhupf/src/Calculate.cpp','libhupf/src/ik.cpp'],
  include_dirs = ['libhupf/inc','libhupf'],
  extra_compile_args=extra_compile_args,
  extra_link_args=['-shared','-lstdc++','-fopenmp'])
      
setup(
  name='libhupf',
  version='0.11',
  packages=['libhupf'],
  cmdclass={
      'build_ext': BuildExt,
      'install'  : PostInstall 
  },
  include_package_data=True,
  ext_modules=[module],
  author = 'Jose Capco',
  data_files = [("", ["license.txt"])]
)
