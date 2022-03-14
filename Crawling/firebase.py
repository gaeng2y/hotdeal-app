import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


def setup():
    cred = credentials.Certificate("fashion-hotdeal-firebase-adminsdk-4j25u-1669072ff8.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL' : 'https://fashion-hotdeal-default-rtdb.firebaseio.com/'   
    })

def update(title, thumbnail, url):
    dir = db.reference()
    dir.push({"title": title,
                "thumbnail": thumbnail,
                "url": url
                })

def get():
    dir = db.reference()
    data = dir.get('/')
    print(data[0])