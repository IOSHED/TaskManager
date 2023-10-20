from django.urls import path

from .view import HomeView

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
]
