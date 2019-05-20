from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item


def homepage(request):
    
    if request.method == 'POST':
        text = request.POST.get('item_text')
        Item.objects.create(text=text)
        return redirect('/')

    return render(request, 'lists/home.html', {'items': Item.objects.all()})