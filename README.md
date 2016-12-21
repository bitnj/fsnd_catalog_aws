# fsnd_item_catalog
FullStack Nanodegree Item Catalog project

This project implements the Item Catalog project from the Udacity Fullstack
Nanodegree according to the rubric provided here: [Project Rubric](https://review.udacity.com/#!/rubrics/5/view)

The project utilizes the following tools:

1. Flask
2. Python
3. SQLAlchemy
4. sqlite3


## Setting up the virtual machine

Development was done using a virtual machine configured by Udacity, which can be
found here [Virtual Machine Repo](https://github.com/bitnj/fullstack-nanodegree-vm/tree/master/vagrant)

Put the pg_config.sh file into the catalog directory.
Type "vagrant init" and when the installation is complete you should have a
Vagrantfile in the directory.  Type "vagrant up" to launch the virtual machine.
When the vm is up type "vagrant ssh" to login.

## Running the application
To run the application change to the /vagrant directory and type python
application.py to start the local server.

In a browser go to localhost:8000 to view the web app.
