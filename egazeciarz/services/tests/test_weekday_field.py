# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError
from django.test import TestCase

from services.fields import WeekdayField


class WeekdayFieldTests(TestCase):

    def test_7_days(self):
        days = range(WeekdayField.MONDAY, len(WeekdayField.DAY_OF_THE_WEEK)+1)
        for day in days:
            field = WeekdayField()
            self.assertEqual(field.clean(day, None), day)

    def test_no_0th_day_in_the_week(self):
        field = WeekdayField()
        with self.assertRaisesMessage(
            ValidationError,
            expected_message=(
                u"Day number should be between 1 and 7"
            )
        ):
            field.clean(0, None)

    def test_no_13th_day_in_the_week(self):
        field = WeekdayField()
        with self.assertRaisesMessage(
            ValidationError,
            expected_message=(
                u"Day number should be between 1 and 7"
            )
        ):
            field.clean(13, None)
