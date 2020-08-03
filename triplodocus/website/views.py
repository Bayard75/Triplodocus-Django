from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt
from .forms import SonForm, SonUpdateForm, EnAvantStyleUpdate

from django.http import JsonResponse
import json

from .models import Son, EnAvantStyle


def acceuil(request):

    current_styles = EnAvantStyle.objects.all().first()

    if request.method == 'POST':
        styles_form = EnAvantStyleUpdate(request.POST, instance=current_styles)
        if styles_form.is_valid():
            styles_form.save()
    styles_form = EnAvantStyleUpdate(instance=current_styles)

    context = {
        'sons': Son.objects.all().order_by('-date_posted'),
        'dernier': Son.objects.exclude(youtube__exact='').exclude(en_avant=True).latest('date_posted'),
        'style': current_styles,
        'stylesUpdateForm': styles_form
    }

    try:
        context['en_avant'] = Son.objects.get(en_avant=True)

    except:
        pass

    return render(request, 'website/acceuil_web.html', context)

@login_required
def edit_song(request, id):

    song = Son.objects.get(id=id)
    if request.method == 'POST':
        song_form = SonForm(request.POST, request.FILES, instance=song)
        if song_form.is_valid():
            song_form.save()
            return redirect('page-admin')

    song_form = SonForm(instance=song)
    context = {
        'song': song,
        'song_form': song_form
    }

    return render(request, 'website/edition.html', context)

@login_required
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

@login_required
@csrf_exempt
def delete_song(request):

    if request.method == 'POST':
        body = json.loads(request.body)
        id = body['id']

        song_to_delete = Son.objects.get(id=id)
        song_to_delete.delete()

        return JsonResponse({'message': 'Le titre a bien été suprimé'})

    return redirect('site-acceuil')


@login_required
@csrf_exempt
def change_en_avant(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        id = body['id']
        ancient_en_avant = Son.objects.get(en_avant=True)
        new_en_avant = Son.objects.get(id=id)

        if new_en_avant.youtube == '':
            return JsonResponse({'message': "Ce titre n'a pas de lien youtube"})
        
        ancient_en_avant.en_avant = False
        ancient_en_avant.save()
        new_en_avant.en_avant = True
        new_en_avant.save()

        return JsonResponse({'ancient': ancient_en_avant.id})

    return render(request, 'website/groupe.html', context)
