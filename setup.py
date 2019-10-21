# https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/quickstart.html

# * How to 'Create Release':
# 	Start with `dev` marker
#	As you work, change the version field to 0.1
#	To create a release, your source code needs to be packaged into a single archive 
# file using the `sdist` command:
#		$ python setup.py sdist
# 	This will create a `dist` subdirectory in your project containing compressed archive files of the source code:
#		TarotDeck808-0.1.tar.gz -- this can be published anywhere!
#   Also creates a MANIFEST file - contains a list of all files inclueded


from distutils.core import setup

setup ( # Describes the metadata about project

	name='TarotDeck808', # Required, unique to PyPI
	version='0.1dev',  # Required *
	packages=['towelstuff',], # Required
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.txt').read(),
)