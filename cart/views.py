from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from menu.models import Dish

from .models import CartItem

# @login_required: ფუნქცია მხოლოდ შესული (ავტორიზებული) მომხმარებლისთვის მუშაობს.
#                  შეუსვლელს Django ავტომატურად შესვლის გვერდზე გადაიყვანს.
# @require_POST:   ფუნქცია მხოლოდ ფორმის გაგზავნაზე (POST) მუშაობს, რადგან მონაცემებს ცვლის.
#                  მისამართის უბრალოდ გახსნით (GET) კალათა არ შეიცვლება.
# request.user:    ის მომხმარებელი, ვინც ახლა შესულია საიტზე.


@login_required
def cart_detail(request):
    """კალათის გვერდი: მომხმარებლის კერძები და ჯამური ფასი."""
    items = CartItem.objects.filter(user=request.user).select_related('dish')
    total = sum(item.subtotal() for item in items)  # ჯამური ფასი ყოველ ჯერზე თავიდან ითვლება
    return render(request, 'cart/cart.html', {'items': items, 'total': total})


@login_required
@require_POST
def add_to_cart(request, dish_id):
    """„კალათაში დამატება“ ღილაკი: თუ კერძი უკვე კალათაშია, რაოდენობას ვზრდით 1-ით."""
    dish = get_object_or_404(Dish, id=dish_id)
    item, created = CartItem.objects.get_or_create(user=request.user, dish=dish)
    if not created:
        item.quantity += 1
        item.save()
    messages.success(request, f'„{dish.name}“ დაემატა კალათაში.')
    # ვბრუნდებით იმავე გვერდზე, საიდანაც დააჭირა (ფილტრებიც შენარჩუნდება)
    return redirect(request.META.get('HTTP_REFERER') or 'menu:dish_list')


@login_required
@require_POST
def increase(request, item_id):
    """„+“ ღილაკი."""
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.quantity += 1
    item.save()
    return redirect('cart:detail')


@login_required
@require_POST
def decrease(request, item_id):
    """„−“ ღილაკი: 1-ზე ნაკლები ვერ იქნება, ამიტომ 1-დან დაკლებისას კერძი იშლება."""
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()
        messages.info(request, f'„{item.dish.name}“ წაიშალა კალათიდან.')
    return redirect('cart:detail')


@login_required
@require_POST
def remove(request, item_id):
    """„წაშლა“ ღილაკი."""
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()
    messages.info(request, f'„{item.dish.name}“ წაიშალა კალათიდან.')
    return redirect('cart:detail')
