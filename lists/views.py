from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from django.views.decorators.http import require_POST


def homepage(request):
    return render(request, 'lists/home.html')

def ViewList(request):
    return render(request, 'lists/list.html', {'items': Item.objects.all()})

@require_POST
def NewList(request):
    Item.objects.create(text=request.POST.get('item_text'))
    return redirect('/lists/the-only-list-in-the-world/')