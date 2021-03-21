from django.urls import path
from . import views

# portfolio urls
urlpatterns = [
    path('', views.index, name='index'),
]
