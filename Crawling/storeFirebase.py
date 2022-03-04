import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("fashion-hotdeal-firebase-adminsdk-4j25u-1669072ff8.json")
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://fashion-hotdeal-default-rtdb.firebaseio.com/'   
})

dir = db.reference()
dir.update({'패션' : '펨코'})