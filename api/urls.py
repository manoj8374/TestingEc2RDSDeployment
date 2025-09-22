from django.urls import path
from . import views


urlpatterns = [
    path('hello', views.hello, name='hello'),
    path('items', views.create_item, name='create_item'),
]


