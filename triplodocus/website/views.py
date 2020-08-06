from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt
from .forms import SonForm, SonUpdateForm, EnAvantStyleUpdate

from django.http import JsonResponse, HttpResponse
from django.core import serializers

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
        'style': current_styles,
        'stylesUpdateForm': styles_form,
    }
    if Son.objects.filter(en_avant=True):
        context['en_avant'] = Son.objects.get(en_avant=True)
    else:
        context['en_avant'] = []
    try:
        context['dernier'] = Son.objects.exclude(youtube__exact='').exclude(en_avant=True).latest('date_posted')
    except:
        context['dernier'] = None

    return render(request, 'website/acceuil_web.html', context)

@login_required
@csrf_exempt
def edit_song(request, id):
    song_to_edit = Son.objects.get(id=id)
    if request.method == 'POST':
        song_form = SonForm(request.POST, request.FILES, instance=song_to_edit)
        if song_form.is_valid():
            song_form.save()
            return redirect('groupe-admin')
        return redirect('site-acceuil')

@login_required
def get_song_infos(request, id):
    if request.method == 'GET':
        song = Son.objects.filter(id=id)
        song_serialized = serializers.serialize('json', song)
        return HttpResponse(song_serialized, content_type="text/json-comment-filtered")
    return redirect('groupe-admin')


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
        ancient_en_avant = Son.objects.filter(en_avant=True)
        new_en_avant = Son.objects.get(id=id)

        if new_en_avant.youtube == '':
            return JsonResponse({'message': "Ce titre n'a pas de lien youtube"})
        
        if not ancient_en_avant:
            new_en_avant.en_avant = True
            new_en_avant.save()
            return JsonResponse({'cas': '1'})

        elif new_en_avant.titre != ancient_en_avant[0].titre:
            ancient_en_avant[0].en_avant = False
            ancient_en_avant[0].save()
            new_en_avant.en_avant = True
            new_en_avant.save()
            return JsonResponse({'ancient': ancient_en_avant[0].id,
                                'cas': '2'})

        else:
            ancient_en_avant[0].en_avant = False
            ancient_en_avant[0].save()
            return JsonResponse({'ancient': ancient_en_avant[0].id,
                                'cas': '3'})

    return render(request, 'website/groupe.html', context)
