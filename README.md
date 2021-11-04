# The Awards
The Awards app

## Author   
>[Aisha Rashid](https://github.com/rashidaysher)  
  
# Description  
This is a awards application built with django.
A user can post their projects, rate other people's projects, comment on it, Post projets and use awards api.
The end points on the Develpoer's page can be used by the user.
  
##  Live Link  
 Click [View Site](https://awards-3590.herokuapp.com/)  to visit the site

## MVPs  
* View different photos posted by other users
* Comment on images  
* Search for project   
* Update your profile.  
  Sign up and log in

  
  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
https://github.com/rashidaysher/awwards_clone_app.git```
##### Navigate into the folder and install requirements  
 ```bash 
cd <created repo> then run: <pipenv install>  to install all the requirements
##### Install and activate Virtual  
 ```bash 
- python3 pipenv shell
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations  
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Running the application  
 ```bash 
 python manage.py server 
```
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3.8](https://www.python.org/)  
* [Django ](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  
  
## Contact Information   
If you have any question or contributions, send a pull request at: [rashidaisha.ara@gmail.com]  
  
## License 
* @MIT Licence
* Copyright (c) 2021 **Rashid Aisha**
