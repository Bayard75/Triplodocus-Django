from django import forms
from .models import Son, EnAvantStyle

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
                  'spotify',
                  'en_avant']

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

class EnAvantStyleUpdate(forms.ModelForm):
    
    class Meta:
        model = EnAvantStyle
        fields = ['banniere_titre',
                'banniere_couleur',
                'banniere_background',
                'couleur_corps',
                'background_corps']