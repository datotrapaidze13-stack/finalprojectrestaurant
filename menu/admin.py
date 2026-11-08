"""
ადმინ პანელის პარამეტრები.

ადმინ პანელი Django-ს ჩაშენებული გვერდია (/admin/), სადაც რესტორნის მფლობელს
კოდის შეცვლის გარეშე შეუძლია კერძების დამატება, რედაქტირება და წაშლა.
აქ მხოლოდ ვეუბნებით, რომელი ცხრილები გამოჩნდეს და რა სვეტებით.
"""

from django.contrib import admin

from .models import Category, Dish


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'spiciness', 'nuts', 'vegetarian']  # სიაში ნაჩვენები სვეტები
    list_filter = ['category', 'spiciness', 'nuts', 'vegetarian']                     # ფილტრები მარჯვნივ
    search_fields = ['name']                                                          # ძებნის ველი
