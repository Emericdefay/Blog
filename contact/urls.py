from django.urls import path

from .views import contactView

app_name = 'contact'

urlpatterns = [
    path('', contactView, name='email'),
]