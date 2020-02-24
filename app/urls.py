from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('signup/', views.signup),
    path('profile/', views.profile),
]