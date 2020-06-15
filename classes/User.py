# -*- coding: utf-8 -*-
""" 
YouTube source: https://www.youtube.com/watch?v=hJ2HfejqppE 

To Fix:
-   nickname and passwords pass as tupple not like string values.
"""
import json
import shelve
from flask import jsonify
from collections import namedtuple

class User:
    def __init__(self, email, nickname, password, first_name, last_name):
        self.email = email
        self.nickname = nickname,
        self.nickname = self.nickname[0]
        self.password = password,
        self.password = self.password[0]
        self.first_name = first_name
        self.last_name = last_name
    
    @classmethod
    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_dict)
    
    @classmethod
    def from_dict(cls, d):
        item = namedtuple("User", d.keys())(*d.values())
        return item
    
    def __repr__(self):
        return "User Object: %s, %s, %s, %s, %s" % (self.email, self.nickname, self.first_name, self.last_name, self.password)


json_string = '''{
    "first_name": "Homer",
    "last_name": "Sanchez",
    "email": "homer@me.com",
    "nickname": "superboy55",
    "password": "d41d8cd98f00b204e9800998ecf8427e"
}'''

#user = User.from_json(json_string)
#print(user)
dict = {'email': 'homer@me.com', 'nickname': 'superboy55', 'password': 'd41d8cd98f00b204e9800998ecf8427e', 'first_name': 'Homer', 'last_name': 'Sanchez'}
res = json.loads(str(dict))
user = User.from_dict(res)
class_vars = vars(User)
class_dict = dict(class_vars)
print(class_dict)