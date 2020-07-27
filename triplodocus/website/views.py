from django.shortcuts import render, redirect
from .models import Son

from django.views.decorators.csrf import csrf_exempt
from .forms import SonForm, SonUpdateForm
from django.http import JsonResponse
import json


def acceuil(request):

    context = {
        'sons': Son.objects.all().order_by('-date_posted'),
        'dernier': Son.objects.exclude(youtube__exact='').exclude(en_avant=True).latest('date_posted')
    }

    try:
        context['en_avant'] = Son.objects.get(en_avant=True)

    except:
        pass

    return render(request, 'website/acceuil_web.html', context)


def admin_page(request):

    if request.method == 'POST':
        song_form = SonForm(request.POST, request.FILES)
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
            'form_song': SonForm,
        }

        return render(request, 'website/groupe.html', context)

@csrf_exempt
def delete_song(request):

    if request.method == 'POST':
        body = json.loads(request.body)
        id = body['id']

        song_to_delete = Son.objects.get(id=id)
        song_to_delete.delete()

        return JsonResponse({'message': 'Le titre a bien été suprimé'})

    return redirect('site-acceuil')

@csrf_exempt
def change_en_avant(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        id = body['id']
        ancient_en_avant = Son.objects.get(en_avant=True)
        new_en_avant = Son.objects.get(id=id)

        ancient_en_avant.en_avant = False
        ancient_en_avant.save()
        new_en_avant.en_avant = True
        new_en_avant.save()

        return JsonResponse({'ancient': ancient_en_avant.id})
    
    return redirect('site-acceuil')
