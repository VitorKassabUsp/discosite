from django.shortcuts import render

from django.http import HttpResponse
from .temp_data import album_data

from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Post

from django.shortcuts import render, get_object_or_404



def list_albuns(request):
    album_list = Post.objects.all()
    context = {'album_list': album_list}
    return render(request, 'albuns/index.html', context)

def detail_album(request, album_id):
    album = get_object_or_404(Post, pk=album_id)
    context = {'album': album}
    return render(request, 'albuns/detail.html', context)



def search_albuns(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        album_list = Post.objects.filter(title__icontains=search_term)
        context = {"album_list": album_list}
    return render(request, 'albuns/search.html', context)

def create_album(request):
    if request.method == 'POST':
        album_title = request.POST['title']
        album_band = request.POST['band']
        album_release_year = request.POST['release_year']
        album_content = request.POST['content']
        
        album_poster_url = request.POST['poster_url']
        album = Post(title=album_title,
                      release_year=album_release_year,
                      poster_url=album_poster_url, band = album_band, content = album_content)
        album.save()
        return HttpResponseRedirect(
            reverse('albuns:detail', args=(album.id, )))
    else:
        return render(request, 'albuns/create.html', {})
    
def update_album(request, album_id):
    album = get_object_or_404(Post, pk=album_id)

    if request.method == "POST":
        album.title = request.POST['title']
        album.content = request.POST['content']
        album.release_year = request.POST['release_year']
        album.band = request.POST['band']
        album.poster_url = request.POST['poster_url']
        album.save()
        return HttpResponseRedirect(
            reverse('albuns:detail', args=(album.id, )))

    context = {'album': album}
    return render(request, 'albuns/update.html', context)


def delete_album(request, album_id):
    album = get_object_or_404(Post, pk=album_id)

    if request.method == "POST":
        album.delete()
        return HttpResponseRedirect(reverse('albuns:index'))

    context = {'album': album}
    return render(request, 'albuns/delete.html', context)