# ESPNPlusPlus
css360 group project

## Running ESPNPlusPlus on your machine
<br />

### Install python3 on your computer if you don't already have it
### Create a virtual environment for our django project using the Python built-in module `venv` below
<br/>

Enter this command in your terminal, one folder level outside from our project folder. We don't want our virtual environment on github. 
<br/>

Im calling the virtual environment virt1, but you can call it anything
```
python3 -m venv virt1
```
<br/>

We do this so that all the dependacies live in the virtual environment, this way other projects you guys make won't interfere with the dependacies version we used on this project.
<br/>

Activate virual environment
This command is for Apple computers (bash/zsh shells)
This is different if your on windows. I can help you if you cant find how.
```
source virt1/bin/activate
```
<br/>

When it's activated youll see it in parenthesis in your terminal path, this is mine
```
~/UWB/Winter23/Software Engineering (virt1)
```
<br/>

To deactivate, enter this command and should look normal again. 
```
deactivate
~/UWB/Winter23/Software Engineering
```
<br/>

## Install all dependacies/packages
<br/>

When your virtual environment is activated, type the following command in the same folder level where you see the `requirements.txt` file
```
pip3 install -r requirements.txt
```
<br/>

This will install everything you need for the django project to run on your computer

<br/>

## Running a mysql database server locally and connecting it via mysql connecter

You'll need to run install all packagers from requriments.txt and install the MySql community edition

here is the link for it if you haven't downloaded the MySql community edition and remember your root password!!
```
https://dev.mysql.com/downloads/installer/
```
Now you can create a local database using MySql Workbench

<br/>

## Hosting this web application locally 

Before hosting the web appplication, you would need to create a database that contains data for the nba players.

You can do so by running nba_database.py, but  it may failed since the API that we are using are super unreliable so

I would recommend to just import the "old_nba_database" into your local mysql database.

Once your database contains the data about the players then you will have to change your mysql root password in settings.py.

After you are all set and you just run python mange.py runserver to host to web app.

<br/>