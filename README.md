Pandas Recipes
=============

> Disclaimer: Pun is always intended!

Virtualenv Setup
=============

	$ mkdir pandas_project && cd !$
	$ mkvirtualenv --no-site-packages `pwd`/pandas_env
	$ source pandas_env/bin/activate

Requirements
=============

+ Install numpy so pip install -r does not fail

		pip install numpy

+ Install with minimum and recommended dependencies

		pip install -r requirements/minimal.txt

+ Install suggested dependencies

		pip install -r requirements/suggested.txt

+ Install SPSS read/write support

		pip install -r requirements/spss.txt

+ Various build dependencies on Debian

		sudo apt-get build-dep python-lxml
		sudo apt-get install libhdf5-dev


