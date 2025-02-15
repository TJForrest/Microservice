# Manages all files for simple project launch. 

# Reference:
# https://setuptools.pypa.io/en/latest/userguide/quickstart.html

# Import set up tools to launch project 
from setuptools import setup 

setup(

	name = "project_car",
	version = "0.1.0",
	package = ["project_car"],
	entry_points = {
		"console_scripts": [
			"procar = project_car.__main__:main"
		]
	}
)

		
