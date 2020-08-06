from django.urls import path
from . import views

urlpatterns = [
    path('', views.acceuil, name="site-acceuil"),
    path('groupe', views.admin_page, name="groupe-admin"),
    path('delete_song', views.delete_song, name="delete-song"),
    path('change_en_avant', views.change_en_avant, name="change-en-avant"),
    path('edit_song/<id>', views.edit_song, name='edit-son'),
    path('get_song_infos/<id>', views.get_song_infos, name='get-song-infos')
]
