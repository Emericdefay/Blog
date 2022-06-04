from django.urls import path

from . import views

app_name = 'resume'

urlpatterns = [
    path('', views.some_view, name='body'),
]