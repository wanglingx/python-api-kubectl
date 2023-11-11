from mongoengine import connect, Document, StringField

class User(Document):
    google_id = StringField(unique=True)
    email = StringField(unique=True)
    name = StringField()
    profile_image = StringField()
