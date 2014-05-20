from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)