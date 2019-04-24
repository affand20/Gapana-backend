import firebase_admin
from firebase_admin import db

firebase_admin.initialize_app(options={
    'databaseURL': 'https://gapana-3283b.firebaseio.com'
})
NEWS = db.reference('news')
USER = db.reference('user')