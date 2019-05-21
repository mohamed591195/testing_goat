from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item


def homepage(request):
    
    if request.method == 'POST':
        text = request.POST.get('item_text')
        Item.objects.create(text=text)
        return redirect('/lists/the-only-list-in-the-world/')

    return render(request, 'lists/home.html')

def ViewList(request):
    return render(request, 'lists/list.html', {'items': Item.objects.all()})