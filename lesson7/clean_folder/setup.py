from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='1',
      description='script for transrer and clean files in foulder',
      url='https://github.com/aaalice47/goit-python/tree/master/lesson7',
      author='Valerii Topchii',
      author_email='wellkswell@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean-folder = clean_folder.clean:clean'],
                    })