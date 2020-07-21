from django.urls import path
from . import views

urlpatterns = [
    path('', views.acceuil, name="site-acceuil"),
    path('groupe', views.admin_page, name="page-admin"),
    path('delete_song', views.delete_song, name="delete-song"),
]
