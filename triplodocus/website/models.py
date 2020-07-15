from django.db import models

#  Create your models here.
#  The only model needed here are songs


class Son(models.Model):
    titre = models.CharField(max_length=255)
    titre_image = models.ImageField(default='default.jpg', upload_to='tire_image')
    poster_image = models.ImageField(default='default.jpg', upload_to='poster_image')
    resume = models.TextField(blank=True)
    realisation = models.TextField(blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    youtube = models.URLField(blank=True)
    deezer = models.URLField(blank=True)
    spotify = models.URLField(blank=True)
    en_avant = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.titre} son model.'

