# fsnd_item_catalog
FullStack Nanodegree Item Catalog project

This project implements the Item Catalog project from the Udacity Fullstack
Nanodegree according to the rubric provided here: [Project Rubric](https://review.udacity.com/#!/rubrics/5/view)

The project utilizes the following tools:

1. Flask
2. Python
3. SQLAlchemy
4. sqlite3
5. WTF-Forms

## Getting started
First download the git repository files and maintain the directory structure.

## Setting up the virtual machine

Development was done using a virtual machine configured by Udacity.  There
should be a pg_config.sh in the catalog directory if you downloaded the git
repository.  Type "vagrant init" and when the installation is complete you should
have a Vagrantfile in the directory.  Type "vagrant up" to launch the virtual
machine.  When the vm is up type "vagrant ssh" to login.

## Running the application

On the virtual machine change to the /vagrant directory and type python
runserver.py to start the local server.

In a browser go to localhost:5000 to view the web app.

## CRUD
Create, Update, and Delete functionality can be accessed through the Edit dropdown menu
in the top navigation bar.  Update and Delete are only visible if a Category or
Item have been selected.  You can return to the home page at any time by
clicking on the CatalogApp or Home menu items in the main navigation bar.
