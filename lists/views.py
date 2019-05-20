from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    
    return render(request, 'lists/home.html', {'new_item_text': request.POST.get('item_text', '')})