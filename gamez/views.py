from site import PREFIXES
from urllib.parse import quote_from_bytes
from django.http import HttpResponse
from django.shortcuts import render
from django.db import models
from django.contrib.auth.decorators import login_required
from .models import Collection, Game, Platform


# The main page that lets users manage their game collection
@login_required
def index(request):
    
    uid = request.user.id
    collection = Collection.objects.filter(user_id=uid).first()
    games = Game.objects.filter(collection_id=collection.id).select_related('platform')

    return render(request, 'gamez/index.html', {'collection': collection, 'games': games})


# The no-login brag page that a user can share with other people
def brag(request, user):
    return render(request, 'gamez/brag.html', {})
