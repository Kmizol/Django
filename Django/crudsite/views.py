from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def livre_create_view(request):
    return render(request, 'crudsite/main.html')