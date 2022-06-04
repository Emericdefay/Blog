from django.urls import path

from .views import contactView, successView

app_name = 'contact'

urlpatterns = [
    path('', contactView, name='email'),
    path('success/', successView, name='success'),
]