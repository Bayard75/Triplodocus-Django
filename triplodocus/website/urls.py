from django.urls import path
from . import views

urlpatterns = [
    path('', views.acceuil, name="site-acceuil"),
    path('groupe', views.admin_page, name="page-admin"),
]
