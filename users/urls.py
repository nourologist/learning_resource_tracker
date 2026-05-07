'''Defines url patterns for users app'''

from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    # Include default auth urls
    path('', include('django.contrib.auth.urls')),
    # Registration page
    path('register/', views.register, name='register',),
    #path('password_change/', views.PasswordChangeView.as_view(success_url='done'), name='password_change'),
]