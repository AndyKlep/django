from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('new', views.new, name='new'),
    path('data', views.data),
    path('test', views.test)
]

