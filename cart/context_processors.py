from django.db.models import Sum

from .models import CartItem


def cart_count(request):
    """რამდენი კერძია კალათაში. ყველა გვერდზე ხელმისაწვდომია (ჰედერში, „კალათა“ ღილაკზე ჩანს).

    settings.py-ში TEMPLATES → context_processors სიაშია ჩამატებული.
    """
    if not request.user.is_authenticated:  # შეუსვლელს კალათა არ აქვს
        return {'cart_count': 0}
    total = CartItem.objects.filter(user=request.user).aggregate(Sum('quantity'))
    return {'cart_count': total['quantity__sum'] or 0}
