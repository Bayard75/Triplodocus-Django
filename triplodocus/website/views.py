from django.shortcuts import render
from .models import Son

import json


def acceuil(request):

    context = {
        'sons': Son.objects.all()
    }
    user_agent = request.headers.get('User-Agent')
    if 'Mobi' in user_agent:
        return render(request, 'website/acceuil_mobile.html', context)

    return render(request, 'website/acceuil_web.html', context)
