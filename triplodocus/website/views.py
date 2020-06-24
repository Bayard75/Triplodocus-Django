from django.shortcuts import render


# Create your views here.
def acceuil(request):
    user_agent = request.headers.get('User-Agent')
    if 'Mobi' in user_agent:
        return render(request, 'website/acceuil_mobile.html')

    return render(request, 'website/acceuil.html')
