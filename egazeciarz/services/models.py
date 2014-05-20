from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)

class User(models.Model):
    pass #service_id = models.

