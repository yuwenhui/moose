import os
import sys
from distutils.sysconfig import get_python_lib

from setuptools import find_packages, setup

overlay_warning = False
if "install" in sys.argv:
    lib_paths = [get_python_lib()]
    if lib_paths[0].startswith("/usr/lib/"):
        # We have to try also with an explicit prefix of /usr/local in order to
        # catch Debian's custom user site-packages directory.
        lib_paths.append(get_python_lib(prefix="/usr/local"))
    for lib_path in lib_paths:
        existing_path = os.path.abspath(os.path.join(lib_path, "moose"))
        if os.path.exists(existing_path):
            # We note the need for the warning here, but present it after the
            # command is run, so it's more likely to be seen.
            overlay_warning = True
            break


EXCLUDE_FROM_PACKAGES = ['moose.conf.project_template',
                         'moose.conf.app_template',
                         'moose.bin']


# Dynamically calculate the version based on django.VERSION.
version = __import__('moose').get_version()


setup(
    name='Moose',
    version=version,
    url='https://github.com/muma378/moose',
    author='Xiao Yang',
    author_email='xiaoyang0117@gmail.com',
    description=('Your manager for endless iterative tasks.'),
    long_description=open('README.md').read(),
    license='BSD',
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    include_package_data=True,
    scripts=['moose/bin/moose-admin.py'],
    entry_points={'console_scripts': [
        'moose-admin = moose.core.management:execute_from_command_line',
    ]},
    install_requires=[
        'opencv-python>=3.3.0.10',
        'Pillow>=3.4.1',
        'MySQL-python>=1.2.5',
        'pymongo>=3.5.1',
        'pymssql>=2.1.3',
        'pysmb>=1.1.17',
        'azure>=2.0.0rc6',
        'chardet>=3.0.4',
    ],
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        "Topic :: Utilities",
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
