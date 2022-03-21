from django import forms
from account.models import User
from django.core.exceptions import ValidationError


class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone', 'email', 'password')

    def clean_email(self):
        email = self.cleaned_data['email']
        customer = User.objects.filter(email=email).exists()
        if customer:
            return ValidationError('this email already exist')
        return email

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        customer = User.objects.filter(phone=phone).exists()
        if customer:
            return ValidationError('this phone already exist')
        return phone


class CustomerLoginForm(forms.Form):
    phone = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
