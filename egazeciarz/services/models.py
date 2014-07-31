from django.contrib.auth.models import User
from django.db import models


class ReceiverType(models.Model):
    receiver = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.receiver


class Hour(models.Model):
    hour = models.TimeField(unique=True)

    def __unicode__(self):
        return u'%s' % self.hour


class Day(models.Model):
    dow = models.CharField(max_length=10, unique=True)

    def __unicode__(self):
        return self.dow


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        unique=True,
        related_name='profile',
    )
    receiver_types = models.ManyToManyField(
        ReceiverType,
        null=True,
        blank=True,
    )

    def display_receiver(self):
        return ','.join([
            ReceiverType.receiver
            for ReceiverType in self.receiver_types.all()
        ])

    display_receiver.short_description = 'Receiver types'
    display_receiver.allow_tags = True

    def __unicode__(self):
        return "Profil: %s" % self.user


def create_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)


class Subscription(models.Model):
    visable_name = models.CharField(max_length=50, unique=True)
    recipe_name = models.CharField(max_length=50)
    website_url = models.URLField()

    def __unicode__(self):
        return self.visable_name


class UsersSubs(models.Model):
    subscription = models.ForeignKey(Subscription, to_field='visable_name')
    user = models.ForeignKey(User, to_field='username')

    def __unicode__(self):
        return u"%s" % self.id


class SubPattern(models.Model):
    sub_id = models.ForeignKey(UsersSubs)
    day_id = models.ForeignKey(Day, to_field='dow')
    hour_id = models.ForeignKey(Hour, to_field='hour')

    def __unicode__(self):
        return u"%s" % self.id


class Service(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name
