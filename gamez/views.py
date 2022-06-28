from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# The main page that lets users manage their game collection
@login_required
def index(request):
    return render(request, 'gamez/index.html')


# The no-login brag page that a user can share with other people
def brag(request, user):
    return render(request, 'gamez/brag.html', {})
