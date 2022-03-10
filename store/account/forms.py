from django import forms
from account.models import Users
from django.core.exceptions import ValidationError


class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('first_name', 'last_name', 'username', 'phone', 'email', 'password')

    def clean_email(self):
        email = self.cleaned_data['email']
        customer = Users.objects.filter(email=email).exists()
        if customer:
            return ValidationError('this email already exist')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        customer = Users.objects.filter(username=username).exists()
        if customer:
            return ValidationError('this username already exist')
        return username

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        customer = Users.objects.filter(email=phone).exists()
        if customer:
            return ValidationError('this phone already exist')
        return phone


class CustomerLoginForm(forms.Form):
    phone = forms.CharField(max_length=30)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
