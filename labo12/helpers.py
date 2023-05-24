# helpers.py
import json
import datetime
import random
import chardet

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        elif isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)

def random():
    return random.randint(0, 100)

def chardet():
    # implementation of chardet function
    pass
