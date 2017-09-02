from django.db import models


class User(models.Model):
    title = models.CharField(max_length=120)
    content = models.CharField(max_length=500)
    last_update = models.DateField()

class post(models.Model):
    title = models.CharField(max_length=120)
    content = models.CharField(max_length=500)
    last_update = models.DateField()
