import setuptools
# Each Python project should have pyproject.toml or setup.py
# TODO: Please create pyproject.toml instead of setup.py (delete the setup.py)
# used by python -m build
# ```python -m build``` needs pyproject.toml or setup.py
# The need for setup.py is changing as of poetry 1.1.0 (including current pre-release) as we have moved away from needing to generate a setup.py file to enable editable installs - We might able to delete this file in the near future
PACKAGE_NAME = "event-meetup-com-selenium-imp-local"
setuptools.setup(
     name = PACKAGE_NAME,
     version='0.0.4',
     author="Circles",
     author_email="info@circles.life",
     # TODO: Please update the description and delete this line
     description="PyPI Package for Circles <project-name> Local/Remote Python",
     # TODO: Please update the long description and delete this line    
     long_description="This is a package for sharing common XXX function used in different repositories",
     long_description_content_type="text/markdown",
     url="https://github.com/circles",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: Other/Proprietary License",
         "Operating System :: OS Independent",
     ],
 )
