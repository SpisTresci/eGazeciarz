from django.test import TestCase
#from django.test.utils import override_settings
from django.contrib.auth import SESSION_KEY


#@override_settings(
#    PASSWORD_HASHERS=('django.contrib.auth.hashers.SHA1PasswordHasher',),
#)
class ChangePasswordTestCase(TestCase):
    # ./manage.py dumpdata --indent 3 auth.user > ./services/fixtures/users.json
    fixtures = ['users.json']

    def login(self, email='test@test.com', password='password'):
        response = self.client.post('/accounts/login/', {
            'login': email,
            'password': password,
        }, follow=True)
        self.assertTrue(SESSION_KEY in self.client.session)
        return response

    def test_change_password_redirects_to_login(self):
        response = self.client.post('/services/password-change/', {
            'password_change-new_password1': 'new_password',
            'password_change-new_password2': 'new_password',
            'password_change-old_password': 'password',
        })
        self.assertRedirects(response, '/accounts/login/')
