from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime, timedelta


# Create your views here.
def index(request):
    user = {
        'id': '123',
        'name': 'Aibek',
        'is_authenticated': True
    }

    context = {
        'user': user,
        'status': 1
    }
    return render(request, 'index.html', context=context)


def time_plus(request):
    if request.GET['hours']:
        dt = datetime.now() + timedelta(hours=int(request.GET['hours']))
        return HttpResponse(dt)
    return HttpResponse('null')


def hours_ahead(request, **kwargs):
    dt = datetime.now() + timedelta(days=kwargs.get('asd'), hours=kwargs.get('asd1'))
    return HttpResponse(dt)
