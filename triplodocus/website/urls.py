from django.urls import path
from . import views

urlpatterns = [
    path('', views.acceuil, name="site-acceuil"),
]
