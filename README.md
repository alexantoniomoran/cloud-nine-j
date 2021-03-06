# Jenna's on Cloud 9??
A website to spread awareness whenever Jen blasts off to Cloud 9


## Locally Set Up Project
1. Create a python 3 virtual environment and pip install the requirements.txt
2. Add all necessary bash_profile vars
3. source ~/.bash_profile
4. source ../[venv_name]/bin/activate
5. python manage.py createsuperuser
6. Make sure the local env var DJANGO_SETTINGS_MODULE is set to website.local_settings (export DJANGO_SETTINGS_MODULE=website.local_settings)


## Locally Run Code
1. python manage.py runserver (use --insecure if not using local settings)


## To Deploy Project to Heroku
Heroku set up following instructions here:
https://www.codementor.io/@jamesezechukwu/how-to-deploy-django-app-on-heroku-dtsee04d4

1. git init
2. git add .
3. git commit -m 'commit'
4. git push heroku master
5. heroku run python manage.py migrate


## Heroku Useful Commands
1. heroku logs --tail
2. heroku run python manage.py migrate
2. heroku run python manage.py createsuperuser


## Heroku Variables to Set
- SECRET_KEY, CLOUD_NAME, CLOUD_API_KEY, CLOUD_API_SECRET


## Set up Domain

Followed article here:
https://dev.to/spyker77/how-to-connect-godaddy-domain-with-heroku-and-cloudflare-mdh

Used Heroku DNS in settings, cloudflare for the DNS, and set up custom DNS on GoDaddy
