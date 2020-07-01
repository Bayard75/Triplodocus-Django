from django.db import models

#  Create your models here.
#  The only model needed here are songs


class Son(models.Model):
    titre = models.CharField(primary_key=True, max_length=255)
    titre_image = models.ImageField(default='default.jpg', upload_to='son_pics')
    poster_image = models.ImageField(default='default.jpg', upload_to='son_poster')
    resume = models.TextField()
    realisation = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    youtube = models.URLField()
    deezer = models.URLField()
    spotify = models.URLField()
    en_avant = models.BooleanField(default=False)
    

    def __str__(self):
        return f'{self.titre} son model.'

