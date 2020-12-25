# Django-Heroku-Student-App

## Dependencies

django-model-utils
django django-heroku gunicorn
git
heroku cli

Fork this repo

create app on heroku
in my case app name is 'your-django-app-name'
create app

Install (Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-command-line)

cmd > heroku login (login with your credentials)
You'll see something like >  Logged in as user@mail.com

## Update your settings.py file

ALLOWED_HOSTS = ['your-django-app-name.herokuapp.com'] #Use your App name at Line 33

## Create git ignore file
Create a .gitignore file in the project root:

`db.sqlite3 
`*.pyc 
`__pycache__/ 
`*.py[cod] 
`.DS_Store

make sure you're in project root directory /Django-Heroku-Student-App



# Custom Chnages
 
clone this repo
 > https://github.com/<your-git-username>/Django-Heroku-Student-App.git

