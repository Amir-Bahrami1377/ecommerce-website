from django.shortcuts import render, redirect
from django.contrib import messages
from account.forms import CustomerRegistrationForm, CustomerLoginForm
from django.views.generic import View
from account.models import Customer


class RegisterView(View):
    class_form = CustomerRegistrationForm

    def get(self, request):
        form = self.class_form
        return render(request, 'account/register.html', {'form': form})

    def post(self, request):
        form = self.class_form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Customer.objects.create(**cd)
            messages.success(request, 'your account created successfully', 'success')
            return redirect('product:products')
        return redirect('accounts:register', 'account/register.html', {'form': form})


class LoginView(View):
    class_form = CustomerLoginForm

    def get(self, request):
        form = self.class_form
        return render(request, 'account/login.html', {'form': form})

    def post(self, request):
        pass
