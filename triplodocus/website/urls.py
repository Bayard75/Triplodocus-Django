from django.urls import path
from . import views

urlpatterns = [
    path('', views.acceuil, name="site-acceuil"),
    path('groupe', views.admin_page, name="page-admin"),
    path('delete_song', views.delete_song, name="delete-song"),
    path('change_en_avant', views.change_en_avant, name="change-en-avant"),
    path('edit/<id>', views.edit_song, name='edit-son')
]
