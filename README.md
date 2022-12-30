## dogsitter

DogSitter is a website that dog owners can use to find available DogSitters in their area. 
### How To Build the Environment
* First clone the environment
```
git clone git@github.com:robyncam/dogsitter.git
```
* Navigate to repository and build virtual env
```
cd dogsitter
python venv env
./env/bin/activate
pip install -r requirements.txt
```
* Create the following credentials in Postgres
```
'NAME': 'dogsitter'
'USER': 'dogsitter_user'
'PASSWORD': 'abcdef'
```
* Run migrations and run site
```
python manage.py migrate
python manage.py runserver
```