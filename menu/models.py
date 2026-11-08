"""
მოდელები = მონაცემთა ბაზის ცხრილები.

თითო კლასი არის ერთი ცხრილი, თითო ველი (name, price...) არის ცხრილის ერთი სვეტი.
Django ამ კლასებიდან თავად ქმნის ცხრილებს ბრძანებით: python manage.py migrate
"""

from django.core.validators import MaxValueValidator
from django.db import models


class Category(models.Model):
    """კერძის კატეგორია, მაგ. „სალათები“, „სუპები“."""

    name = models.CharField('დასახელება', max_length=100, unique=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'კატეგორია'
        verbose_name_plural = 'კატეგორიები'

    def __str__(self):
        return self.name


class Dish(models.Model):
    """ერთი კერძი მენიუში."""

    # ForeignKey = კავშირი სხვა ცხრილთან: ყოველი კერძი ერთ კატეგორიას ეკუთვნის
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='dishes', verbose_name='კატეგორია')
    name = models.CharField('დასახელება', max_length=150)
    price = models.DecimalField('ფასი', max_digits=8, decimal_places=2)
    # სურათის მისამართი static ფოლდერში, მაგ. images/dishes/tom_yam.png
    image = models.CharField('სურათის ფაილი', max_length=300, blank=True)
    spiciness = models.PositiveSmallIntegerField(
        'სიცხარე',
        default=0,
        validators=[MaxValueValidator(4)],  # მაქსიმუმ 4
        help_text='0 - არ არის ცხარე, 4 - ძალიან ცხარე',
    )
    nuts = models.BooleanField('ნიგვზიანი', default=False)
    vegetarian = models.BooleanField('ვეგეტარიანული', default=False)

    class Meta:
        ordering = ['category', 'id']
        verbose_name = 'კერძი'
        verbose_name_plural = 'კერძები'

    def __str__(self):
        return self.name
