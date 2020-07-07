from django.shortcuts import render
from .models import Son

import json


def acceuil(request):

    context = {
        'sons': Son.objects.all().order_by('-date_posted'),
        'en_avant': Son.objects.get(en_avant=True),
        'dernier': Son.objects.latest('date_posted')
    }

    return render(request, 'website/acceuil_web.html', context)

def admin_page(request):

    context = {
        'sons': Son.objects.all().order_by('-en_avant','-date_posted')
    }

    return render(request, 'website/groupe.html', context)
