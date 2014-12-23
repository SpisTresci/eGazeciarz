from django.contrib.auth.models import User
from django.db import models
from services.fields import WeekdayField, SharpHourField


class Service(models.Model):
    name = models.CharField(max_length=100, unique=True)
    recipe_name = models.CharField(max_length=50)
    website_url = models.URLField()

    def __unicode__(self):
        return self.name


class UsersSubs(models.Model):
    service = models.ForeignKey(Service, to_field='name')
    user = models.ForeignKey(User, to_field='username')

    def __unicode__(self):
        return u"%s" % self.id


class SubPattern(models.Model):
    users_subs = models.ForeignKey(UsersSubs)
    weekday = WeekdayField()
    hour = SharpHourField()

    def __unicode__(self):
        return u"%s" % self.id
