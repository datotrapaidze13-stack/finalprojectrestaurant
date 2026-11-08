from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm

# ყველა მისამართი იწყება /accounts/-ით (იხ. restaurant/urls.py)
urlpatterns = [
    # რეგისტრაცია: ჩვენი დაწერილი ფუნქცია
    path('register/', views.register, name='register'),
    # შესვლა და გამოსვლა: Django-ს მზა გვერდები, მხოლოდ ჩვენს შაბლონსა და ფორმას ვაძლევთ
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
