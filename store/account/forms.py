from django import forms
from account.models import Customer
from django.core.exceptions import ValidationError


class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'username', 'phone', 'email', 'password')

    def clean_email(self):
        email = self.cleaned_data['email']
        customer = Customer.objects.filter(email=email).exists()
        if customer:
            return ValidationError('this email already exist')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        customer = Customer.objects.filter(username=username).exists()
        if customer:
            return ValidationError('this username already exist')
        return username

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        customer = Customer.objects.filter(email=phone).exists()
        if customer:
            return ValidationError('this phone already exist')
        return phone


class CustomerLoginForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('phone', 'password')
