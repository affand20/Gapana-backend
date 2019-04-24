import firebase_admin
from firebase_admin import db

firebase_admin.initialize_app(options={
    'apiKey': "AIzaSyAADa1e4P9WSU8xXcidzOaqrqN5DTrbJ4Q",
    'authDomain': "gapana-3283b.firebaseapp.com",
    'databaseURL': "https://gapana-3283b.firebaseio.com",
    'projectId': "gapana-3283b",
    'storageBucket': "gapana-3283b.appspot.com",
    'messagingSenderId': "407432302370",
})
NEWS = db.reference('news')
USER = db.reference('user')


def _ensure_hero(ids):
    hero = NEWS.child(ids).get()
    if not hero:
        return
    return hero


def viewnews():
    return NEWS.get()


def addnews(data):
    return NEWS.push(data)


def updatenews(ids, data):
    _ensure_hero(ids)
    NEWS.child(ids).update(data)


def deletenews(ids):
    _ensure_hero(ids)
    NEWS.child(ids).delete()
