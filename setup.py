# https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/quickstart.html

# Setup.py describes the metadata about project

# Required fields are:
# 	- name (must be unique in PyPI)
#  	- version
#	- packages (where you put Python source code)
# 	- ...


from distutils.core import setup

setup (
	name='TowelStuff',
	version='0.1dev',
	packages=['towelstuff',],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.txt').read(),
)