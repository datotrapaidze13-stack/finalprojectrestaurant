"""
ავტომატური ტესტები: ამოწმებს, რომ ფილტრები სწორად მუშაობს.
გაშვება: python manage.py test

ტესტისთვის Django ცალკე, ცარიელ ბაზას ქმნის, ამიტომ ნამდვილ მონაცემებს არ ეხება.
"""

from django.test import TestCase

from .models import Category, Dish


class DishFilterTests(TestCase):
    def setUp(self):
        # სატესტო მონაცემები: 2 კატეგორია და 3 კერძი
        salads = Category.objects.create(name='სალათები')
        self.soups = Category.objects.create(name='სუპები')
        Dish.objects.create(category=salads, name='ცეზარი', price=12, spiciness=0)
        Dish.objects.create(category=salads, name='ნიგვზიანი სალათი', price=9, spiciness=1, nuts=True, vegetarian=True)
        Dish.objects.create(category=self.soups, name='ტომ იამი', price=7, spiciness=3)

    def get_names(self, params):
        """ხსნის მთავარ გვერდს მოცემული ფილტრებით და აბრუნებს ნაჩვენები კერძების სახელებს."""
        response = self.client.get('/', params)
        self.assertEqual(response.status_code, 200)
        return {dish.name for dish in response.context['dishes']}

    def test_without_filters_all_dishes_are_shown(self):
        self.assertEqual(self.get_names({}), {'ცეზარი', 'ნიგვზიანი სალათი', 'ტომ იამი'})

    def test_category(self):
        self.assertEqual(self.get_names({'category': self.soups.id}), {'ტომ იამი'})

    def test_spiciness(self):
        self.assertEqual(self.get_names({'spiciness': 3}), {'ტომ იამი'})

    def test_no_nuts(self):
        self.assertEqual(self.get_names({'no_nuts': 'on'}), {'ცეზარი', 'ტომ იამი'})

    def test_vegetarian(self):
        self.assertEqual(self.get_names({'vegetarian': 'on'}), {'ნიგვზიანი სალათი'})

    def test_filters_work_together(self):
        self.assertEqual(self.get_names({'spiciness': 0, 'no_nuts': 'on'}), {'ცეზარი'})
