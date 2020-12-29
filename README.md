# Django-Heroku-Student-App

## Dependencies

`1` django-model-utils <br>
`2` django django-heroku gunicorn <br>
`3` git <br>
`4` heroku cli <br>

# Fork this repo

## Create app on heroku

in my case app name is > 'your-heroku-app-name'

## Install Git & Heroku

Install [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-command-line)

## Login Heroku (terminal)

> heroku login 

(login with your credentials)

You'll see something like >  Logged in as user@mail.com

## Update your settings.py file

ALLOWED_HOSTS = ['your-heroku-app-name.herokuapp.com'] #Use your App name at Line 33

## Create git ignore file
Create a .gitignore file in the project root:

db.sqlite3 <br>
*.pyc <br>
__pycache__/ <br>
*.py[cod] <br>
.DS_Store<br>

make sure you're in project root directory /Django-Heroku-Student-App and your heroku is logged in

> git add .

> git commit -m "test django app"

> git push

#Connect your Git repo with Heroku

https://dashboard.heroku.com/apps/(your-heroku-app-name)/deploy/github  #your app name

Click on Connect to GitHub under Deployment method Section

connect your github profile

search > Django-Heroku-Student-App

Connect your Git repo

Deploy Branch

## if collectstatic error

try on console with heroky login <br>
> heroku config:set DISABLE_COLLECTSTATIC=1 --app 'your-heroku-app-name'

# Make Migrations

> heroku run python manage.py makemigrations --app 'your-heroku-app-name' <br>
> heroku run python manage.py migrate --app 'your-heroku-app-name'

# Create SuperUser

> heroku run python manage.py createsuperuser --app 'your-heroku-app-name'


# Custom Chnages

heroku git:remote -a your-heroku-app-name 
git push heroku main



 
# clone this repo
 
 > [Django Heroku Student App](https://github.com/mustafaali96/Django-Heroku-Student-App)

