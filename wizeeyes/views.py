from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render
from .models import Glasses

def glasses(request):
    data = Glasses.objects.all();
    return render(request, 'wizeeyes/glasses.html', {'glasses': data})

def home(request):
    return HttpResponse("Home page")

def glasses_detail(request, id):
    data = Glasses.objects.get(pk=id)
    return render(request, 'wizeeyes/detail.html', {'spx': data})

def add(request):
    title = request.POST.get('title')
    price = request.POST.get('price')

    if title and price:
        spx = Glasses(title=title, price=price)
        spx.save()
        return HttpResponseRedirect('/glasses')

    return render(request, 'wizeeyes/add.html')

def delete(request, id):
    try:
        spx = Glasses.objects.get(pk=id)
    except:
        raise Http404('Spx does not exist.')

    spx.delete()

    return HttpResponseRedirect('/glasses')
