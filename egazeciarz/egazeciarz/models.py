# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver


class ReceiverType(models.Model):
    """
    Type of internet-service/tool/device supported by eGazeciarz, which is
    able to receive newspapers/articles send by eGazeciarz.

    Fields:
    ;type: as described above.

    ;receiver_id: - email address/account key/id  - proper id of specified
    service which unequivocally determines recipient.

    """
    EMAIL = 1
    KINDLE = 2
    RECEIVER_TYPES = (
        (EMAIL, 'E-mail'),
        (KINDLE, 'Kindle'),
    )

    type = models.IntegerField(choices=RECEIVER_TYPES, default=KINDLE)
    receiver_id = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return "%s %s" % (self.type, self.receiver_id)


class UserProfile(models.Model):
    """
    "Extension", additional fields, attached by 1-1 relation directly to
    django.contrib.auth.models.User.
    """
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
            reviver_type.receiver
            for reviver_type in self.receiver_types.all()
        ])

    display_receiver.short_description = 'Receiver types'
    display_receiver.allow_tags = True

    def __unicode__(self):
        return "Profil: %s" % self.user


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)
