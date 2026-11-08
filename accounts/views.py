from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect, render

from .forms import RegisterForm


def register(request):
    """რეგისტრაციის გვერდი.

    GET  (გვერდის გახსნა)      → ვაჩვენებთ ცარიელ ფორმას
    POST (ღილაკზე დაჭერა)      → ვამოწმებთ ფორმას:
         სწორია   → ვქმნით მომხმარებელს, ვაშვებთ სისტემაში და მთავარ გვერდზე გადაგვყავს
         არასწორია → იგივე ფორმას ვაჩვენებთ შეცდომებით
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # რეგისტრაციისთანავე შეგვყავს სისტემაში
            messages.success(request, 'რეგისტრაცია წარმატებით დასრულდა!')
            return redirect('menu:dish_list')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})
