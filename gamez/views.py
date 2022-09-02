import hashlib
import pickle
import base64
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import User, Collection, Game, Platform


# The main page that lets users manage their game collection
# Vulnerability: the key is generated from user id, easy to decode and tamper
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
def bragView(request, key):

    collection = Collection.objects.filter(key=key).first()
    games = Game.objects.filter(collection_id=collection.id).select_related('platform')

    return render(request, 'gamez/brag.html', {'collection': collection, 'games': games})


# Delete a game from a collection
# Vulnerability: possibility to delete other people's games because the object's owner is not checked
@login_required
def deleteView(request, id):

    obj = get_object_or_404(Game, id=id)
    obj.delete()

    return redirect(indexView)


# On this page the users can add new games
# Vulnerability: collection id is passed through the form, can be tampered
@login_required
def newView(request):

    uid = request.user.id
    collection = Collection.objects.filter(user_id=uid).first()
    platforms = Platform.objects.all()

    return render(request, 'gamez/new.html', {'collection': collection, 'platforms': platforms})


# Add a game to a collection
# Vulnerability: possibility to add games to other people's collections because the ownership of collection is not checked
@login_required
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


# Lets the customer to download a backup of his game collection
@login_required
def backupView(request):

    uid = request.user.id

    collection = Collection.objects.filter(user_id=uid).first()
    games = Game.objects.filter(collection_id=collection.id).select_related('platform')

    output = base64.b64encode(pickle.dumps(games))
    
    response = HttpResponse(output)
    response['Content-Type'] = 'text/plain; charset=utf-8'
    response['Content-Disposition'] = 'attachment; filename=backup.txt'

    return response


# Lets the customer to upload a backup file of his game collection
@login_required
def uploadView(request):
    return render(request, 'gamez/upload.html')


# Processes the uploaded backup file
# Vulnerability: pickle payloads can be tampered easily, the code below will execute OS commands (RCE)
@login_required
def restoreView(request):

    file = base64.b64decode(request.FILES['file'].read())
    games = pickle.loads(file)
    
    # The actual restore function has not been implemented
    # The purpose is to demonstrate the exploit which is triggered by pickle.loads(), i.e. already when loading the data

    return redirect(indexView)
