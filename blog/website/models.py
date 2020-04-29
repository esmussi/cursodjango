from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    content = models.TextField()

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=200)