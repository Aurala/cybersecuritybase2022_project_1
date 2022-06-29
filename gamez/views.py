from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Collection, Game, Platform


# The main page that lets users manage their game collection
@login_required
def indexView(request):
    
    uid = request.user.id
    collection = Collection.objects.filter(user_id=uid).first()
    games = Game.objects.filter(collection_id=collection.id).select_related('platform')

    return render(request, 'gamez/index.html', {'collection': collection, 'games': games})


# The no-login brag page that a user can share with other people
def bragView(request, user):
    return render(request, 'gamez/brag.html', {})


# Delete a game from a collection
# Vulnerability: possibility to delete other people's games because the object's owner is not checked
def deleteView(request, id):
    obj = get_object_or_404(Game, id=id)
    obj.delete()
    return redirect(indexView)


# On this page the users can add new games
def newView(request):
    return render(request, 'gamez/new.html', {})


# Add a game to a collection
# Vulnerability: possibility to add games to other people's collections because the ownership of collection is not checked
def addView(request, collection, thumbnail, info, platform, rating):
    return redirect(indexView)