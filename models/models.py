import firebase_admin
from firebase_admin import db

firebase_admin.initialize_app(options={
    'databaseURL': 'https://<DB_NAME>.firebaseio.com'
})
SUPERHEROES = db.reference('superheroes')