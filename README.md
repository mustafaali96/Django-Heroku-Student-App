# Django-Heroku-Student-App

## Dependencies

`1` django-model-utils <br>
`2` django django-heroku gunicorn <br>
`3` git <br>
`4` heroku cli <br>

# Fork this repo

## Create app on heroku

in my case app name is > 'your-django-app-name'

## Install Git & Heroku

Install [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-command-line)

## Login Heroku (terminal)

> heroku login 

(login with your credentials)

You'll see something like >  Logged in as user@mail.com

## Update your settings.py file

ALLOWED_HOSTS = ['your-django-app-name.herokuapp.com'] #Use your App name at Line 33

## Create git ignore file
Create a .gitignore file in the project root:

`` db.sqlite3 
`` *.pyc 
`` __pycache__/ 
~ *.py[cod] 
~ .DS_Store

make sure you're in project root directory /Django-Heroku-Student-App and your heroku is logged in

> git add .

> git commit -m "test django app"

> git push


# Custom Chnages
 
clone this repo
 > [mustafaali96/Django-Heroku-Student-App](https://github.com/<your-git-username>/Django-Heroku-Student-App.git)

