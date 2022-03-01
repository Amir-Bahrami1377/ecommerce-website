from django import forms
from account.models import Customer


class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'username', 'phone', 'email', 'password')


class CustomerLoginForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('phone', 'password')
