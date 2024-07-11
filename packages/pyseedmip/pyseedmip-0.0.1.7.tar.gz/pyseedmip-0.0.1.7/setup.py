from setuptools import setup, Extension, find_packages
import os
import sys
from setuptools.command.install import install

import sysconfig

class CustomInstallCommand(install):
    def run(self):
        env = os.environ
        bin_path = ''

        module_path = sysconfig.get_path('purelib', 'posix_user')
        if 'root/.local' in module_path:
            module_path = module_path.replace('root/.local','usr/local')
        
        # 判断是否在虚拟环境
        if "CONDA_PREFIX" in env:
            module_path = os.path.join(env["CONDA_PREFIX"], "lib/")

        if "lib/" in module_path:
          bin_path = module_path.split("lib/")[0]
          bin_path = os.path.join(bin_path, 'bin/')
        else:
          raise Exception('Cannot determine binary file installation path from module path')

        # 创建所需目录并复制文件
        if not os.path.exists(bin_path):
            os.makedirs(bin_path)

        # 这里假设要复制的文件在 lib_file_path 和 bin_file_path 路径下
        bin_file_path = 'license/build/seedmip_actv'  # 请替换为实际的二进制文件路径
        
        os.system(f"cp {bin_file_path} {bin_path}")

        install.run(self)


setup(
    name="pyseedmip",
    version="0.0.1.7",
    aduthor="seed",
    description="seedmip for python",
    packages=find_packages(),   # automatically find all python packages
    package_data={'pyseedmip': ['pyseedmip.cpython-39-x86_64-linux-gnu.so']},
    cmdclass={
        'install': CustomInstallCommand,
    },
)
