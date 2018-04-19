from __future__ import unicode_literals
from ..login.models import Users
from django.db import models

class CourseManager(models.Manager):
    def validate(self, data):
        errors = []
        if len(data['name']) < 5:
            errors.append('Course name must be atleast 5 characters.')
        if len(data['name']) >255:
            errors.append('Course name cannot be longer than 255 characters.')
        if len(data['desc']) < 15:
            errors.append('Course description must be atleast 15 characters.')
        if len(data['desc']) >255:
            errors.append('Course description cannot be longer than 255 characters.')
        return errors
        

class Courses(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(Users, related_name="created_course")
    attendees = models.ManyToManyField(Users, related_name="courses")
    objects = CourseManager()