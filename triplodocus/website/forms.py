from django import forms
from .models import Son

class SonForm(forms.ModelForm):

    class Meta:
        model = Son
        fields = ['titre',
                  'titre_image',
                  'poster_image',
                  'resume',
                  'realisation',
                  'youtube',
                  'deezer',
                  'spotify']

class SonUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Son

        fields = ['titre',
                  'titre_image',
                  'poster_image',
                  'resume',
                  'realisation',
                  'youtube',
                  'deezer',
                  'spotify']