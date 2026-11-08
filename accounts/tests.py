"""
ავტომატური ტესტები: რეგისტრაცია და შესვლა.
გაშვება: python manage.py test
"""

from django.contrib.auth.models import User
from django.test import TestCase


class AccountTests(TestCase):
    def register(self, email, password1, password2=None):
        return self.client.post('/accounts/register/', {
            'email': email,
            'password1': password1,
            'password2': password2 or password1,
        })

    def test_register_creates_user_and_logs_in(self):
        response = self.register('Nika@Mail.com', 'paroli123')
        self.assertRedirects(response, '/')
        user = User.objects.get()
        self.assertEqual(user.email, 'nika@mail.com')    # ელფოსტა პატარა ასოებით ინახება
        self.assertNotEqual(user.password, 'paroli123')  # პაროლი დაშიფრულია, არა ღია ტექსტი
        self.assertTrue(self.client.get('/').context['user'].is_authenticated)

    def test_same_email_twice(self):
        self.register('nika@mail.com', 'paroli123')
        self.client.logout()
        response = self.register('nika@mail.com', 'sxvaparoli1')
        self.assertContains(response, 'ამ ელფოსტით მომხმარებელი უკვე არსებობს.')
        self.assertEqual(User.objects.count(), 1)

    def test_short_password(self):
        response = self.register('nika@mail.com', '123')
        self.assertContains(response, 'პაროლი მინიმუმ 8 სიმბოლოსგან უნდა შედგებოდეს.')
        self.assertFalse(User.objects.exists())

    def test_passwords_do_not_match(self):
        response = self.register('nika@mail.com', 'paroli123', 'paroli456')
        self.assertContains(response, 'ორი პაროლის ველი ერთმანეთს არ ემთხვევა')
        self.assertFalse(User.objects.exists())

    def test_login_and_logout(self):
        User.objects.create_user('nika@mail.com', 'nika@mail.com', 'paroli123')
        response = self.client.post('/accounts/login/', {'username': 'nika@mail.com', 'password': 'paroli123'})
        self.assertRedirects(response, '/')
        self.client.post('/accounts/logout/')
        self.assertFalse(self.client.get('/').context['user'].is_authenticated)

    def test_wrong_password(self):
        User.objects.create_user('nika@mail.com', 'nika@mail.com', 'paroli123')
        response = self.client.post('/accounts/login/', {'username': 'nika@mail.com', 'password': 'arasworia'})
        self.assertContains(response, 'ელფოსტა ან პაროლი არასწორია.')
