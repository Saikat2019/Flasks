# Flasks
To run python flask I will suggest to use virtual environment
  to create virtual environment in linux follow the following steps
 ## This is for python 3.5 which is installed in ubuntu 16.04 by default
 1. create a new virtual environment by
     ## virtualenv nameOfyourFolder
 2. then go to the folder 
     ## cd nameOfyourFolder
 3. then activate the virtual environment by
     ## source bin/activate
 4. then install flask by
     ## pip3 install flask
     
# But For python 3.6 this is some different

  1. first we need to install python 3.6
    ##  sudo add-apt-repository ppa:jonathonf/python-3.6 
   ## sudo apt-get update
   ## sudo apt-get install python3.6
   
 2. now to create a python 3.6 virtual environment
    ## virtualenv -p /usr/bin/python3.6(path where python 3.6 is installed) ~/virtualenvs/venv_devopspy(name of the virtual folder
    ## source virtualenvs/venv_devopspy/bin/activate
    
 ## Important
 
    ## while installind something in python 3.6 virtual env ... we should use pip3.6 install packagename instead of pip3 install
