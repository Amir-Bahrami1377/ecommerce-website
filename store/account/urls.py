from django.urls import path
from account.views import CustomerRegisterView, CustomerLoginView, CustomerLogoutView, CustomerProfileView


app_name = 'accounts'

urlpatterns = [
    path('register/', CustomerRegisterView.as_view(), name='customer_register'),
    path('login/', CustomerLoginView.as_view(), name='customer_login'),
    path('logout/', CustomerLogoutView.as_view(), name='customer_logout'),
    path('profile/', CustomerProfileView.as_view(), name='customer_profile')
]
