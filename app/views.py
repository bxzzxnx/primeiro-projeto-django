from django.shortcuts import render
from django.http import HttpResponse
from .models import User
# Create your views here.


def users(request):
    users = User.objects.all()
    return render(request, 'index.html', {'Usuário': users})
