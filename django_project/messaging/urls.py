from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name='messaging-home'),
        path('about/', views.about, name='messaging-about'),
]
