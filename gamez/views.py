import hashlib
import pickle
import base64
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import User, Collection, Game, Platform


# The main page that lets users manage their game collection
@login_required
def indexView(request):
    
    uid = request.user.id
    
    # When a new user logs in, a game collection needs to be created
    if Collection.objects.filter(user_id=uid).first() == None:
        key = hashlib.sha256(str(uid).encode('utf-8')).hexdigest()
        collection = Collection(user=User.objects.get(id=uid), name="My Awesome Game Collection", key=key)
        collection.save()
    
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

    uid = request.user.id
    collection = Collection.objects.filter(user_id=uid).first()
    platforms = Platform.objects.all()

    return render(request, 'gamez/new.html', {'collection': collection, 'platforms': platforms})


# Add a game to a collection
# Vulnerability: possibility to add games to other people's collections because the ownership of collection is not checked
def addView(request):

    collection = request.POST.get('collection')
    thumbnail = request.POST.get('thumbnail')
    info = request.POST.get('info')
    name = request.POST.get('name')
    platform = request.POST.get('platform')
    rating = request.POST.get('rating')

    game = Game(collection=Collection.objects.get(id=collection), thumbnail=thumbnail, info=info, name=name, platform=Platform.objects.get(id=platform), rating=rating)
    game.save()
    
    return redirect(indexView)


# Let's the customer to download a backup of his game collection
def backupView(request):

    uid = request.user.id

    collection = Collection.objects.filter(user_id=uid).first()
    games = Game.objects.filter(collection_id=collection.id).select_related('platform')

    output = base64.b64encode(pickle.dumps(games))
    
    response = HttpResponse(output)
    response['Content-Type'] = 'text/plain; charset=utf-8'
    response['Content-Disposition'] = 'attachment; filename=backup.txt'

    return response


# Let's the customer to upload a backup file of his game collection
def uploadView(request):
    return render(request, 'gamez/upload.html')


# Processes the uploaded backup file
def restoreView(request):

    file = base64.b64decode(request.FILES['file'].read())
    games = pickle.loads(file)
    
    # The actual restore function has not been implemeted
    # The purpose is to demonstrate the exploit which is triggered by pickle.loads(), i.e. in preparing the data

    return redirect(indexView)
