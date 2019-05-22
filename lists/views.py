from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item, List
from django.views.decorators.http import require_POST


def homepage(request):
    return render(request, 'lists/home.html')

def ViewList(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'lists/list.html', {'items': Item.objects.filter(list=list_id),
                                               'list': list_
                                               })

@require_POST
def NewList(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST.get('item_text'), list=list_)
    return redirect(f'/lists/{list_.id}/')


def AddItem(request, list_id):
    list_ = List.objects.get(id=list_id)
    text = request.POST.get('item_text')
    Item.objects.create(text=text, list=list_)
    return redirect(f'/lists/{list_.id}/')