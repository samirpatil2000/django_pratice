from django.shortcuts import render
from .models import Song
# Create your views here.
def songIndex(request):
    songs = Song.objects.all()
    #areas = place.area.all()

    context = {
        "songs": songs,
       # "areas": areas,
    }
    return render(request,'uttu_1/song_index.html',context)