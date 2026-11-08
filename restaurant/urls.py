"""
მთავარი მისამართების (URL) ფაილი.

როცა ბრაუზერი რომელიმე მისამართს ითხოვს, Django აქ ეძებს, რომელ აპლიკაციას გადასცეს მოთხოვნა.
"""

from django.contrib import admin
from django.urls import include, path

# ადმინ პანელის სათაური
admin.site.site_header = 'Step Ordering - მართვის პანელი'
admin.site.site_title = 'Step Ordering'
admin.site.index_title = 'რესტორნის მართვა'

urlpatterns = [
    path('', include('menu.urls')),       # მთავარი გვერდი: კერძები და ფილტრები
    path('cart/', include('cart.urls')),  # კალათის გვერდი
    path('accounts/', include('accounts.urls')),  # რეგისტრაცია, შესვლა, გამოსვლა
    path('admin/', admin.site.urls),      # ადმინ პანელი (კერძების დამატება/რედაქტირება)
]
