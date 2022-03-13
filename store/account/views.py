from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from account.forms import CustomerRegistrationForm, CustomerLoginForm
from django.views.generic import View
from account.models import Users


class CustomerRegisterView(View):
    class_form = CustomerRegistrationForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('product:home')
        else:
            return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.class_form
        return render(request, 'account/register.html', {'form': form})

    def post(self, request):
        form = self.class_form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Users.objects.create_user(**cd)
            messages.success(request, 'your account created successfully', 'success')
            return redirect('product:home')
        return render(request, 'account/register.html', {'form': form})


class CustomerLoginView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('product:home')
        else:
            return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = CustomerLoginForm()
        return render(request, 'account/login.html', {'form': form})

    def post(self, request):
        form = CustomerLoginForm(request.POST)
        print(form.errors.as_data())
        if form.is_valid():
            print('11111111111')
            cd = form.cleaned_data
            user = authenticate(request, phone=cd['phone'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'you logged in successfully', 'success')
                return redirect('product:home')
            messages.error(request, 'phone or password wrong', 'warning')
        return render(request, 'account/login.html', {'form': form})


class CustomerLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'you logged out successfully', 'success')
        return redirect('product:home')


class CustomerProfileView(LoginRequiredMixin, View):
    def get(self, request):
        phone = get_user(request)
        user = Users.objects.get(phone=phone)
        return render(request, 'account/profile.html', {'user': user})

