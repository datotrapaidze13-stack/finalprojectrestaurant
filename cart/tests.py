"""
ავტომატური ტესტები: ამოწმებს კალათას (დამატება, +/−, წაშლა, ჯამი).
გაშვება: python manage.py test
"""

from decimal import Decimal

from django.contrib.auth.models import User
from django.test import TestCase

from menu.models import Category, Dish

from .models import CartItem


class CartTests(TestCase):
    def setUp(self):
        category = Category.objects.create(name='სალათები')
        self.salad = Dish.objects.create(category=category, name='ცეზარი', price=Decimal('12.50'))
        self.soup = Dish.objects.create(category=category, name='სუპი', price=Decimal('7.00'))
        self.user = User.objects.create_user('nika@mail.com', 'nika@mail.com', 'paroli123')
        self.client.force_login(self.user)  # ტესტში მომხმარებელი „შეგვყავს“ საიტზე

    def add(self, dish):
        self.client.post(f'/cart/add/{dish.id}/')

    def test_add_and_total(self):
        self.add(self.salad)
        self.add(self.salad)  # მეორედ დამატება რაოდენობას ზრდის, ახალ ჩანაწერს არ ქმნის
        self.add(self.soup)
        response = self.client.get('/cart/')
        self.assertEqual(len(response.context['items']), 2)
        self.assertEqual(response.context['total'], Decimal('32.00'))  # 12.50×2 + 7

    def test_increase_and_decrease(self):
        self.add(self.salad)
        item = CartItem.objects.get()
        self.client.post(f'/cart/{item.id}/increase/')
        self.assertEqual(CartItem.objects.get().quantity, 2)
        self.client.post(f'/cart/{item.id}/decrease/')
        self.client.post(f'/cart/{item.id}/decrease/')  # 1-დან დაკლება კერძს შლის
        self.assertFalse(CartItem.objects.exists())

    def test_remove(self):
        self.add(self.salad)
        item = CartItem.objects.get()
        self.client.post(f'/cart/{item.id}/remove/')
        self.assertFalse(CartItem.objects.exists())

    def test_each_user_has_own_cart(self):
        self.add(self.salad)
        other = User.objects.create_user('ana@mail.com', 'ana@mail.com', 'paroli123')
        self.client.force_login(other)
        response = self.client.get('/cart/')
        self.assertEqual(len(response.context['items']), 0)

    def test_cannot_change_someone_elses_cart(self):
        self.add(self.salad)
        item = CartItem.objects.get()
        other = User.objects.create_user('ana@mail.com', 'ana@mail.com', 'paroli123')
        self.client.force_login(other)
        response = self.client.post(f'/cart/{item.id}/remove/')
        self.assertEqual(response.status_code, 404)  # სხვისი ჩანაწერი „ვერ მოიძებნა“
        self.assertTrue(CartItem.objects.exists())

    def test_guest_is_sent_to_login(self):
        self.client.logout()
        response = self.client.get('/cart/')
        self.assertRedirects(response, '/accounts/login/?next=/cart/')

    def test_opening_add_link_does_not_change_cart(self):
        # „დამატება“ მხოლოდ POST-ით მუშაობს; ბმულის უბრალოდ გახსნა (GET) აკრძალულია
        response = self.client.get(f'/cart/add/{self.salad.id}/')
        self.assertEqual(response.status_code, 405)
        self.assertFalse(CartItem.objects.exists())
