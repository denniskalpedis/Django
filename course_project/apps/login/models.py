from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def reg_validation(self, data):
        errors= []
        if len(data['f_name']) < 2 or len(data['l_name']) < 2:
            errors.append('Name fields cannot be blank.')
        if not data['f_name'].isalpha() or not data['l_name'].isalpha():
            errors.append('Names must only be letters.')
        if len(data['password']) < 8 or len(data['c_password']) < 8:
            errors.append('Password must be atleast 8 characters.')
        if not data['password'] == data['c_password']:
            errors.append('Passwords do not match.')
        if not EMAIL_REGEX.match(data['email']):
            errors.append('Not a valid email address.')
        if self.filter(email=data['email']).count() > 0:
            errors.append('That user already exists.')
        return errors
    def validation(self, data):
        errors= []
        if self.filter(email=data['email']).count()<1:
            errors.append('Incorrect user or password.')
            return errors
        user = self.get(email=data['email'])
        if  not bcrypt.checkpw(data['password'].encode(), user.password.encode()):
            errors.append('Incorrect user or password.')
        return errors


        

class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
