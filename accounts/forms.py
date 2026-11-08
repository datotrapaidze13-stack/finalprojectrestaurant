"""
რეგისტრაციისა და შესვლის ფორმები.

ორივე Django-ს მზა ფორმიდან არის „მემკვიდრეობით“ აღებული (UserCreationForm, AuthenticationForm).
ჩვენ მხოლოდ ვცვლით: სახელის (username) ნაცვლად ელფოსტას ვითხოვთ და ტექსტები ქართულად გვაქვს.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    """რეგისტრაცია: ელფოსტა + პაროლი + პაროლის გამეორება."""

    email = forms.EmailField(label='ელფოსტა')

    class Meta:
        model = User
        fields = ['email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = 'პაროლი'
        self.fields['password1'].help_text = 'მინიმუმ 8 სიმბოლო.'
        self.fields['password2'].label = 'გაიმეორეთ პაროლი'
        self.fields['password2'].help_text = ''

    def clean_email(self):
        """ვამოწმებთ, ეს ელფოსტა უკვე ხომ არ არის დარეგისტრირებული."""
        email = self.cleaned_data['email'].lower()
        if User.objects.filter(username=email).exists():
            raise forms.ValidationError('ამ ელფოსტით მომხმარებელი უკვე არსებობს.')
        return email

    def clean_password1(self):
        password = self.cleaned_data['password1']
        if len(password) < 8:
            raise forms.ValidationError('პაროლი მინიმუმ 8 სიმბოლოსგან უნდა შედგებოდეს.')
        return password

    def save(self, commit=True):
        # Django-ს მომხმარებელს აუცილებლად სჭირდება username, ამიტომ მასში ელფოსტას ვწერთ
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()  # პაროლი ბაზაში დაშიფრული სახით ინახება (ამას Django თავად აკეთებს)
        return user


class LoginForm(AuthenticationForm):
    """შესვლა: ელფოსტა + პაროლი."""

    username = forms.EmailField(label='ელფოსტა', widget=forms.EmailInput(attrs={'autofocus': True}))

    error_messages = {
        'invalid_login': 'ელფოსტა ან პაროლი არასწორია.',
        'inactive': 'ეს ანგარიში გათიშულია.',
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].label = 'პაროლი'

    def clean_username(self):
        return self.cleaned_data['username'].lower()
