from django.shortcuts import render

from django.http import HttpResponse
from .temp_data import album_data

from django.http import HttpResponseRedirect
from django.urls import reverse




def detail_album(request, album_id):
    context = {'album': album_data[album_id - 1]}
    return render(request, 'albuns/detail.html', context)

def list_albuns(request):
    context = {"album_list": album_data}
    return render(request, 'albuns/index.html', context)

def search_albuns(request):
    context = {}
    if request.GET.get('query', False):
        context = {
            "album_list": [
                m for m in album_data
                if request.GET['query'].lower() in m['name'].lower()
            ]
        }
    return render(request, 'albuns/search.html', context)

def create_album(request):
    if request.method == 'POST':
        album_data.append({
            'name': request.POST['name'],
            'release_year': request.POST['release_year'],
            'poster_url': request.POST['poster_url']
        })
        return HttpResponseRedirect(
            reverse('albuns:detail', args=(len(album_data), )))
    else:
        return render(request, 'albuns/create.html', {})