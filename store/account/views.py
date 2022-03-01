from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from account.forms import CustomerRegistrationForm, CustomerLoginForm
from django.views.generic import View
from account.models import Customer


class CustomerRegisterView(View):
    class_form = CustomerRegistrationForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('product:products')
        else:
            return super().dispatch(request, *args, **kwargs)

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
        return render(request, 'account/register.html', {'form': form})


class CustomerLoginView(View):
    class_form = CustomerLoginForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('product:products')
        else:
            return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.class_form
        return render(request, 'account/login.html', {'form': form})

    def post(self, request):
        form = self.class_form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, phone=cd['phone'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'you logged in successfully', 'success')
                return redirect('product:products')
            messages.error(request, 'phone or password wrong', 'warning')
        return render(request, 'account/login.html', {'form': form})


class CustomerLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'you logged out successfully', 'success')
        return redirect('product:products')
