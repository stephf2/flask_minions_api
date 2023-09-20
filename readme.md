
Learning flask, practising to build API with flask and python

- `pip install pipenv`
- `pipenv shell`
- `pipenv install && pipenv install --dev`

Create .env file
```
SQLALCHEMY_DATABASE_URI=protocol://username:password@location/databasename
```
- `pipenv run seed`

- `pipenv run dev`

endpoints:
- `/`
- `/minions`
- `/minions/:id`
- `/minions/:name` (case sensitive)
# flask_minions_api
