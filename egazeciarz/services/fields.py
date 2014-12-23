# -*- coding: utf-8 -*-
"""
This file contains custom definition of Django Model Fields
"""

from django.core.exceptions import ValidationError
from django.db.models import PositiveSmallIntegerField
from django.core import validators
from django.db.models.fields import TimeField
from django.utils.six import string_types

_ = lambda x: x


class RangeValidator(object):
    """
    Validates whether proper value belongs to specified range
    """
    def __init__(self, bottom_limit, top_limit, message, code):
        self.bottom_limit = bottom_limit
        self.top_limit = top_limit
        self.message = message
        self.code = code

    def __call__(self, value):
        if not self.bottom_limit <= value <= self.top_limit:
            raise ValidationError(self.message, code=self.code)


class WeekdayField(PositiveSmallIntegerField):
    """
    Weekday field - simple Integer based field, to store number of the week.
    First day of the week is Monday, which is represented by number 1.
    """

    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

    DAY_OF_THE_WEEK = (
        (MONDAY, _('Monday')),
        (TUESDAY, _('Tuesday')),
        (WEDNESDAY, _('Wednesday')),
        (THURSDAY, _('Thursday')),
        (FRIDAY, _('Friday')),
        (SATURDAY, _('Saturday')),
        (SUNDAY, _('Sunday')),
    )

    default_validators = [
        RangeValidator(
            bottom_limit=MONDAY,
            top_limit=SUNDAY,
            message=_(
                'Day number should be between {} and {}'.format(MONDAY, SUNDAY)
            ),
            code=_('wrong day number')
        )
    ]


class SharpHourValidator(validators.RegexValidator):
    """
    Validates, whether time has minutes and seconds set to 0.
    """
    regex = r'^([01]?[0-9]|2[0-3])(?::00(?::00)?)?$'
    message = _(
        'Enter a valid sharp hour. Correct format is (HH[:00[:00[.000000]]])'
    )
    code = _('not supported time format')


class SharpHourField(TimeField):
    """
    datetime.datetime based field, which accepts only sharp hours.
    Accepted format: HH[:00[:00[.000000]]]
    Examples:
        5
        09
        12
        4:00
        19:00
        00:00:00
        23:00:00.000000
    """

    default_validators = [
        SharpHourValidator(),
    ]

    def to_python(self, value):
        if isinstance(value, string_types) and 1 <= len(value) <= 2:
            if 0 <= int(value) < 24:
                return super(SharpHourField, self).to_python(
                    "{}:00".format(value)
                )

            raise ValidationError(
                SharpHourValidator.message,
                SharpHourValidator.code,
            )
        else:
            return super(SharpHourField, self).to_python(value)
