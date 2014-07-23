from django.contrib.auth.models import User
from django.db import models


class ReceiverType(models.Model):
    receiver = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.receiver


class Hours(models.Model):
    hours = models.TimeField(unique=True)

    def __unicode__(self):
        return u'%s' % self.hours


class Days(models.Model):
    dow = models.CharField(max_length=10, unique=True)

    def __unicode__(self):
        return self.dow


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        unique=True,
        related_name='profile',
    )
    receiver_type = models.ManyToManyField(
        ReceiverType,
        null=True,
        blank=True,
    )

    def display_receiver(self):
        return ','.join([
            ReceiverType.receiver
            for ReceiverType in self.receiver_type.all()
        ])

    display_receiver.short_description = 'Receiver types'
    display_receiver.allow_tags = True

    def __unicode__(self):
        return "Profil: %s" % self.user


def create_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)


class Subscriptions(models.Model):
    visable_name = models.CharField(max_length=50, unique=True)
    reciper_name = models.CharField(max_length=50)
    website_url = models.URLField()

    def __unicode__(self):
        return self.visable_name


class UserSubs(models.Model):
    subscriptions = models.ForeignKey(Subscriptions, to_field='visable_name')
    user = models.ForeignKey(User, to_field='username')

    def __unicode__(self):
        return u"%s" % self.id


class SubPattern(models.Model):
    sub_id = models.ForeignKey(UserSubs)
    day_id = models.ForeignKey(Days, to_field='dow')
    hour_id = models.ForeignKey(Hours, to_field='hours')

    def __unicode__(self):
        return u"%s" % self.id


class Service(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name
