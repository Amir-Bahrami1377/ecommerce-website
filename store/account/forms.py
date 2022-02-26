from django import forms


class CustomerRegistrationForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()


class CustomerLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
