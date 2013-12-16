Pandas Recipes
=============

> Disclaimer: Pun is always intended!

Virtualenv Setup
=============

    mkdir pandas_project && cd pandas_project 
	mkvirtualenv --no-site-packages `pwd`/pandas_env
	source pandas_env/bin/activate

Clone the repository
=============

    git clone https://github.com/madflow/pandas-recipes.git

Requirements
=============

+ Install with minimum and recommended dependencies

        for package in $(cat pandas-recipes/requirements/minimal.txt); do pip install "$package"; done 

+ Install suggested dependencies

        for package in $(cat pandas-recipes/requirements/suggested.txt); do pip install "$package"; done 

+ Install SPSS read/write support

        for package in $(cat pandas-recipes/requirements/spss.txt); do pip install "$package"; done 

+ Install visualization tools

        for package in $(cat pandas-recipes/requirements/visualization.txt); do pip install "$package"; done 

 + Install ipython notebook

        for package in $(cat pandas-recipes/requirements/notebook.txt;) do pip install "$package"; done 

 + Install everything and get it over with

        for package in $(cat pandas-recipes/requirements/*.txt); do pip install "$package"; done 

+ Various build dependencies on Debian

		sudo apt-get build-dep python-lxml
		sudo apt-get install libhdf5-dev python-dev


