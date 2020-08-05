import os
import mock

import json
from django.test import TestCase

from django.urls import reverse
from .models import Son, EnAvantStyle

from django.core.files.images import ImageFile
from django.contrib.auth.models import User

from .forms import SonForm, EnAvantStyleUpdate
from urllib.parse import urlencode
# Create your tests here.


class SonModelTestCase(TestCase):

    def setUp(self):
        titre_image = mock.MagicMock(spec=ImageFile)
        poster_image = mock.MagicMock(spec=ImageFile)
        titre_image.name = 'test_image.jpg'
        poster_image.name = 'test_poster_image.jpg'

        self.son = Son.objects.create(
                        titre='test_titre',
                        resume='resume blabla',
                        realisation='realiser pour test',
                        youtube='https://www.youtube.com/embed/-iNWEwLfkv8',
                        deezer='www.deezer.com',
                        spotify='www.spotify.com',
                        en_avant=True
        )
        self.son.titre_image = titre_image
        self.son.poster_image = poster_image

    def test_son_created(self):
        self.assertTrue(Son.objects.filter(titre='test_titre').exists())

    def test_son_data_exact(self):

        self.assertEqual(self.son.titre_image.name, 'test_image.jpg')
        self.assertEqual(self.son.poster_image.name, 'test_poster_image.jpg')

        self.assertEqual(self.son.resume, 'resume blabla')
        self.assertEqual(self.son.realisation, 'realiser pour test')
        self.assertEqual(self.son.youtube, 'https://www.youtube.com/embed/-iNWEwLfkv8')
        self.assertEqual(self.son.deezer, 'www.deezer.com')
        self.assertEqual(self.son.spotify, 'www.spotify.com')
        self.assertTrue(self.son.en_avant)


class HomePageTestCase(TestCase):

    def setUp(self):
        titre_image = mock.MagicMock(spec=ImageFile)
        poster_image = mock.MagicMock(spec=ImageFile)
        titre_image.name = 'test_image.jpg'
        poster_image.name = 'test_poster_image.jpg'

        self.son = Son.objects.create(
                        titre='test_titre',
                        resume='resume blabla',
                        realisation='realiser pour test',
                        youtube='https://www.youtube.com/embed/-iNWEwLfkv8',
                        deezer='www.deezer.com',
                        spotify='www.spotify.com',
                        en_avant=True
        )
        self.son.titre_image = titre_image
        self.son.poster_image = poster_image

    def test_home_page_return_200(self):
        response = self.client.get(reverse('site-acceuil'))
        self.assertEqual(response.status_code, 200)


class GroupePageTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='usernameTest',
                                             email='testEmail@gmail.com',
                                             password='test2341')

    def test_unauthantifacted_redirects(self):
        reponse = self.client.get(reverse('groupe-admin'))
        self.assertRedirects(reponse, reverse('connexion')+'?next=/groupe')

    def test_groupe_page_return_200(self):
        self.client.login(username='usernameTest', password='test2341')
        response = self.client.get(reverse('groupe-admin'))
        self.assertEqual(response.status_code, 200)


class EditDeleteSongTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='usernameTest',
                                             email='testEmail@gmail.com',
                                             password='test2341')

        titre_image = mock.MagicMock(spec=ImageFile)
        poster_image = mock.MagicMock(spec=ImageFile)
        titre_image.name = 'test_image.jpg'
        poster_image.name = 'test_poster_image.jpg'

        self.son = Son.objects.create(
                        titre='test_titre',
                        resume='resume blabla',
                        realisation='realiser pour test',
                        youtube='https://www.youtube.com/embed/-iNWEwLfkv8',
                        deezer='www.deezer.com',
                        spotify='www.spotify.com',
                        en_avant=False
        )

        self.son.titre_image = titre_image
        self.son.poster_image = poster_image

    def test_delete_song(self):
        self.client.login(username='usernameTest', password='test2341')
        song_to_delete_id = str(self.son.id)
        body = {'id': song_to_delete_id}

        response = self.client.post(reverse('delete-song'),
                                    json.dumps(body),
                                    content_type='application/json')

        self.assertFalse(Son.objects.filter(id=song_to_delete_id).exists())

    def test_change_en_avant(self):
        self.client.login(username='usernameTest', password='test2341')
        song_to_change = str(self.son.id)
        body = {'id': song_to_change}

        response = self.client.post(reverse('change-en-avant'),
                                    json.dumps(body),
                                    content_type='application/json')

        self.assertTrue(self.son.en_avant)
    

class AddingSongTestCase(TestCase):

    def setUp(self):

        titre_image = mock.MagicMock(spec=ImageFile)
        poster_image = mock.MagicMock(spec=ImageFile)
        titre_image.name = 'test_image.jpg'
        poster_image.name = 'test_poster_image.jpg'
        self.form_data = urlencode({'titre': 'new_song',
                     'titre_image': titre_image,
                     'poster_image': poster_image,
                     'realisation': 'new realisation',
                     'youtube': 'www.youtube.com',
                     'deezer': 'www.deezer.com',
                     'spotify': 'www.spotify.com'})

        self.user = User.objects.create_user(username='usernameTest',
                                             email='testEmail@gmail.com',
                                             password='test2341')

    def test_add_song(self):
        self.client.login(username='usernameTest', password='test2341')

        response = self.client.post(reverse('groupe-admin'),
                                    self.form_data,
                                    content_type='application/x-www-form-urlencoded')
        
        self.assertTrue(Son.objects.filter(titre='new_song').exists())

class EditingHomePageTestCase(TestCase):
    
    def setUp(self):
        self.styles = EnAvantStyle.objects.create()
        self.user = User.objects.create_user(username='usernameTest',
                                             email='testEmail@gmail.com',
                                             password='test2341')

    def test_edit_styles(self):
        self.client.login(username='usernameTest', password='test2341')
        form_data = urlencode({'banniere_titre': 'test_titre'})
        self.assertEqual(self.styles.banniere_titre,'NOTRE PREMIER CLIP')

        response = self.client.post(reverse('site-acceuil'),
                                    form_data,
                                    content_type='application/x-www-form-urlencoded')
        
        styles = EnAvantStyle.objects.all().first()
        self.assertEqual(styles.banniere_titre, 'test_titre')

