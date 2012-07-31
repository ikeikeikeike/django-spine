# import sys
import os
from distutils.sysconfig import get_python_lib
from setuptools import (
#    find_packages,
    setup
)


version = '0.3.3'
name = 'django-spine'
short_description = 'Spine plugin for Django'
long_description = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()


def fullsplit(path, result=None):
    """
    Split a pathname into components (the opposite of os.path.join) in a
    platform-neutral way.
    """
    if result is None:
        result = []
    head, tail = os.path.split(path)
    if head == '':
        return [tail] + result
    if head == path:
        return result
    return fullsplit(head, [tail] + result)


packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir != '':
    os.chdir(root_dir)
extensions_dir = 'spine'
data_dir = get_python_lib()

for dirpath, dirnames, filenames in os.walk(extensions_dir):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'):
            del dirnames[i]
    if '__init__.py' in filenames:
        packages.append('.'.join(fullsplit(dirpath)))
    else:
        data_files.append([os.path.join(data_dir, dirpath), [os.path.join(dirpath, f) for f in filenames]])


setup(
    name=name,
    version=version,
    description=short_description,
    long_description=long_description,
    classifiers=[
       # "Development Status :: 3 - Alpha",
       "Development Status :: 4 - Beta",
       "Framework :: Django",
       'Environment :: Console',
       "Environment :: Web Environment",
       "Intended Audience :: Developers",
       'License :: OSI Approved :: MIT License',
       "Programming Language :: Python :: 2.6",
       "Programming Language :: Python :: 2.7",
       'Topic :: Utilities',
       'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords=['javascript', 'coffeescript', 'django', 'spine'],
    author='Tatsuo Ikeda',
    author_email='jp.ne.co.jp at gmail',
    url='https://github.com/ikeikeikeike/django-spine',
    license='MIT License',
#    packages=find_packages(),
#    include_package_data=True,
    packages=packages,
    data_files=data_files,
    install_requires=['django-subcommand', "django-pipeline<=1.2.14", "eco", "bpmappers"],
    # cmdclass={'test': pytest_test},
    # tests_require=['pytest'],
)
