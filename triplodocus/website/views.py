from django.shortcuts import render, redirect
from .models import Son
from django.views.decorators.csrf import csrf_exempt
from .forms import SonForm
import json


def acceuil(request):

    context = {
        'sons': Son.objects.all().order_by('-date_posted'),
        'en_avant': Son.objects.get(en_avant=True),
        'dernier': Son.objects.latest('date_posted')
    }

    return render(request, 'website/acceuil_web.html', context)


def admin_page(request):

    if request.method == 'POST':
        song_form = SonForm(request.POST, request.FILES)
        print(song_form)
        if song_form.is_valid():
            song_form.save()
            context = {
                'sons': Son.objects.all().order_by('-en_avant','-date_posted'),
                'form_song': SonForm
            }
            return render(request, 'website/groupe.html', context)
    else:
        song_form = SonForm
        context = {
            'sons': Son.objects.all().order_by('-en_avant','-date_posted'),
            'form_song': SonForm
        }

        return render(request, 'website/groupe.html', context)