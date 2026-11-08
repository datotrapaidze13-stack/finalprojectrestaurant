"""
View = ფუნქცია, რომელიც იღებს ბრაუზერის მოთხოვნას (request) და აბრუნებს პასუხს (HTML გვერდს).
"""

from django.shortcuts import render

from .models import Category, Dish


def dish_list(request):
    """მთავარი გვერდი: კერძების სია და ფილტრები.

    ფილტრები მისამართში მოდის, მაგ: /?category=2&spiciness=1&no_nuts=on&vegetarian=on
    request.GET ამ პარამეტრებს ლექსიკონის (dict) მსგავსად გვაძლევს.
    """
    dishes = Dish.objects.all()  # ჯერ ყველა კერძი, შემდეგ ფილტრებით ვავიწროებთ

    # კატეგორიის ფილტრი
    category = request.GET.get('category', '')
    if category.isdigit():
        dishes = dishes.filter(category_id=category)

    # სიცხარის ფილტრი (0-4); ცარიელი = „არ არის არჩეული“
    spiciness = request.GET.get('spiciness', '')
    if spiciness.isdigit():
        dishes = dishes.filter(spiciness=spiciness)

    # „ნიგვზის გარეშე“: მონიშნულ checkbox-ს ბრაუზერი აგზავნის როგორც "on"
    if request.GET.get('no_nuts'):
        dishes = dishes.filter(nuts=False)

    # „მხოლოდ ვეგეტარიანული“
    if request.GET.get('vegetarian'):
        dishes = dishes.filter(vegetarian=True)

    # context = მონაცემები, რომლებსაც HTML შაბლონს გადავცემთ
    context = {
        'categories': Category.objects.all(),
        'dishes': dishes,
        'selected_category': category,
        'selected_spiciness': spiciness,
        'spiciness_levels': ['0', '1', '2', '3', '4'],
    }
    return render(request, 'menu/dish_list.html', context)
