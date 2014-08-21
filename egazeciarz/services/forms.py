#! -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User


class ChangeUserEmailForm(forms.ModelForm):

    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', ]

    def clean_password(self):
        password = self.cleaned_data.get('password', None)
        if not self.instance.check_password(password):
            raise forms.ValidationError(
                self.error_messages['password_incorrect'],
                code='password_incorrect'
            )
        return password
