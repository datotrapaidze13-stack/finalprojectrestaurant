from django.contrib.auth.models import User
from django.db import models

from menu.models import Dish


class CartItem(models.Model):
    """ერთი ჩანაწერი კალათაში: ვისი კალათაა, რომელი კერძი და რამდენი ცალი.

    მაგალითად: „nika@mail.com-ის კალათაში ტომ იამი, 2 ცალი“.
    User არის Django-ს მზა მომხმარებლების ცხრილი (რეგისტრაციისას იქ იწერება ახალი მომხმარებელი).
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='მომხმარებელი')
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, verbose_name='კერძი')
    quantity = models.PositiveIntegerField('რაოდენობა', default=1)

    class Meta:
        ordering = ['id']
        verbose_name = 'კალათის ჩანაწერი'
        verbose_name_plural = 'კალათის ჩანაწერები'

    def __str__(self):
        return f'{self.dish} × {self.quantity}'

    def subtotal(self):
        """ამ კერძის ჯამი = ფასი × რაოდენობა."""
        return self.dish.price * self.quantity
