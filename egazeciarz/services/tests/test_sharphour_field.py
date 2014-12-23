# -*- coding: utf-8 -*-
"""
Tests of custom Django Model Field - SharpHourField
"""
import datetime

from django.core.exceptions import ValidationError
from django.test import TestCase

from services.fields import SharpHourField


class SharpHourFieldTests(TestCase):

    def test_valid_format_invalid_time(self):
        """
        Invalid time with proper format should raise ValidationError directly
        from TimeField
        """
        hour = '53:01'
        field = SharpHourField()

        with self.assertRaisesMessage(
            ValidationError,
            expected_message=(
                u"'{}' value has the correct format (HH:MM[:ss[.uuuuuu]]) "
                u"but it is an invalid time.".format(hour)
            )
        ):
            field.clean(hour, None)

    def test_invalid_time_format(self):
        """
        Invalid time format should raise ValidationError directly
        from TimeField. Hours/Minutes/Seconds should be separated by ':'
        """
        hour = '23.01'
        field = SharpHourField()

        with self.assertRaisesMessage(
            ValidationError,
            expected_message=(
                u"'{}' value has an invalid format. It must be "
                u"in HH:MM[:ss[.uuuuuu]] format.".format(hour)
            )
        ):
            field.clean(hour, None)

    def test_invalid_sharp_time(self):
        """
        Valid time entry, which is not representing sharp hour, should raise
        ValidationError from SharpHourValidator
        """
        hour = '23:05'
        field = SharpHourField()

        with self.assertRaisesMessage(
            ValidationError,
            expected_message=(
                u"Enter a valid sharp hour. "
                u"Correct format is (HH[:00[:00[.000000]]])"
            )
        ):
            field.clean(hour, None)

    def test_valid_sharp_time(self):
        """
        All valid sharp time formats should be represented by
        datatime.time objects, with minutes/seconds set to 0
        """
        for hour in ['23', '23:00', '23:00:00', '23:00.00.000000']:
            field = SharpHourField()
            self.assertEqual(field.clean(hour, None), datetime.time(23, 0, 0))

        for hour in ['09', '09:00', '09:00:00', '09:00.00.000000']:
            field = SharpHourField()
            self.assertEqual(field.clean(hour, None), datetime.time(9, 0, 0))

        for hour in ['4', '4:00', '4:00:00', '4:00.00.000000']:
            field = SharpHourField()
            self.assertEqual(field.clean(hour, None), datetime.time(4, 0, 0))
