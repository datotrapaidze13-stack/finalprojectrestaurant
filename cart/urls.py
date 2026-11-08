from django.urls import path

from . import views

app_name = 'cart'

# ყველა მისამართი იწყება /cart/-ით (იხ. restaurant/urls.py)
urlpatterns = [
    path('', views.cart_detail, name='detail'),                           # /cart/
    path('add/<int:dish_id>/', views.add_to_cart, name='add'),            # /cart/add/5/
    path('<int:item_id>/increase/', views.increase, name='increase'),     # /cart/3/increase/
    path('<int:item_id>/decrease/', views.decrease, name='decrease'),     # /cart/3/decrease/
    path('<int:item_id>/remove/', views.remove, name='remove'),           # /cart/3/remove/
]
