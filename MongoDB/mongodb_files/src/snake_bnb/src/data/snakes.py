# %load ./mongodb_files/src/snake_bnb/src/data/snakes.py

import datetime
import mongoengine

# This is a class that defines the snake document
class Snake(mongoengine.Document):
    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    species = mongoengine.StringField(required=True)

    length = mongoengine.FloatField(required=True)
    name = mongoengine.StringField(required=True)
    is_venomous = mongoengine.BooleanField(required=True)

    meta = {
        'db_alias': 'core', # goes into the core
        'collection': 'snakes' # where the collection is stored
    }
