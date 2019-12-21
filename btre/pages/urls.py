from django.urls import path

from . import views
# Create your tests here.

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about')
]