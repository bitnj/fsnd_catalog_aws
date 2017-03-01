# Udacity FullStack Linux Server Config Project

## Overview
See Project Rubric [here]

## Server Setup
1. Change root password using `passwd` command
2. Create a new user using `adduser` [username]
  	- give sudo permission by creating an entry for the new user in the file **/etc/sudoers.d**
  		- [username] ALL=(ALL) NOPASSWD:ALL
3.  Copy the udacity_key.rsa file to the new user
	- ```mkdir /home/grader/.ssh```
    - ```cp ~/.ssh/authorized_keys /home/grader/.ssh/authorized_keys```
    - give owenership and change permissions of the .ssh and authorized_keys file to grader
    	- ```chown grader:grader /home/grader/.ssh```
    	- ```chmod 700 /home/grader/.ssh```
    	- ```chown grader:grader /home/grader/.ssh/authorized_keys```
    	- ```chmod 600 /home/grader/.ssh/authorized_keys```
    - test login as new user
    	- login as new user ```ssh grader@35.161.39.217 -p 2200 -i ~/.ssh/udacity_key.rsa```

4. Update all currently installed packages
    - ```sudo apt-get update```
    - ```sudo apt-get upgrade```
5.  set timezone to UTC
    - ```sudo dpkg-reconfigure tzdata```
    	- follow instructions on GUI to choose timezone
6. SSH Configuration
    - ```sudo vim /etc/ssh/sshd_config```
    - ```change the SSH port 2200```
    - ```reload ssh```
    - log back in at port 2200
7. Firewall Configuration
	- ```sudo ufw default deny incoming```
    - ```sudo ufw default allow outgoing```
    - ```sudo ufw allow ssh```
    - ```sudo ufw allow 2200/tcp```
    - ```sudo ufw allow www```
    - ```sudo ufw allow ntp```
    - ```sudo ufw enable```

8. Disable root access from SSH
	- ```sudo vim /etc/ssh/sshd_config```
		- replace what follows PermitRootLogin with no

## Getting the application running
1. Install Apache
    - ```sudo apt-get install apache2```
    - test correct installation 
    	- in a browser type in the server ip address and the Apache2 Ubuntu Default page will render
2. Install mod-wsgi
    - ```sudo apt-get install libapache2-mod-wsgi```

3. In the **/etc/apache2/sites-enabled** I created a file called **fsnd_item_catalog.conf**
	- view the file for complete setup
		- includes, among other things, **WSGIScriptAlias / /var/www/html/fsnd_item_catalog.wsgi**
4. restart Apache `sudo apache2ctl restart`
5. Install and configure Postgresq5.
	- ```sudo apt-get install postgresql```
    - do not allow remote connections to the database.  This is the default for PostgreSQL when installed from repositories
6. create catalog ROLE. 
	- First, switch to the superuser **postgres**
	- ```sudo -u postgres -i```
	- ```createuser catalog```

To login as a user when the username does match the ROLE within postgres
- ```psql user_name -h 127.0.0.1 -d database_name```

7. Install Git
	- ```sudo apt-get install git-all```
	- Clone the Git repository for the catalog item app in the **/var/www/html** directory
		- ```sudo git clone url_to_repository```

8. Install Flask
	- ```sudo apt-get install python-pip```
	- ```sudo pip install flask```

9. Install SQLAlchemy
	- ```sudo pip install sqlalchemy```

10. Install libraries needed by app
	- ```sudo pip install flask_uploads```
	- ```sudo apt-get install python-dev```
	- ```sudo apt-get install libpq-dev```
	- ```sudo pip install -U psycopg2```

## Resources Used

1. Udacity Class videos
2. Udacity Forums for the project which had links to useful information
3. Stack Overflow
4. Digital Ocean
