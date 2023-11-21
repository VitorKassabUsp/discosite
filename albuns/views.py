from django.shortcuts import render

from django.http import HttpResponse
from .temp_data import album_data

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

'''def list_albuns(request):
    album_list = Post.objects.all()
    context = {'album_list': album_list}
    return render(request, 'albuns/index.html', context)
'''
class PostListView(ListView):
    model = Post
    template_name = 'albuns/index.html'
    context_object_name = 'album_list'

'''def detail_album(request, album_id):
    album = get_object_or_404(Post, pk=album_id)
    context = {'album': album}
    return render(request, 'albuns/detail.html', context)
'''
class PostDetailView(DetailView):
    model = Post
    template_name = 'albuns/detail.html'
    context_object_name = 'album'
    pk_url_kwarg = 'album_id'

'''def search_albuns(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        album_list = Post.objects.filter(title__icontains=search_term)
        context = {"album_list": album_list}
    return render(request, 'albuns/search.html', context)
'''
class PostSearchView(ListView):
    model = Post
    template_name = 'albuns/search.html'
    context_object_name = 'album_list'

    def get_queryset(self):
        query = self.request.GET.get('query', '')
        if query:
            return Post.objects.filter(title__icontains=query.lower())
        else:
            return Post.objects.none()
        
'''def create_album(request):
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
        form = PostForm()
        context = {'form': form}
        return render(request, 'albuns/create.html', context)
 ''' 
class PostCreateView(CreateView): 
    model = Post
    form_class = PostForm
    template_name = 'albuns/create.html'
    success_url = reverse_lazy('albuns:create')

    def form_valid(self, form):
        response = super().form_valid(form)
        # Após criar o post, redirecione para os detalhes do post recém-criado
        return HttpResponseRedirect(reverse('albuns:detail', args=(self.object.id,)))

'''
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
'''
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'albuns/update.html'
    context_object_name = 'album'

    def get_success_url(self):
        return reverse_lazy('albuns:detail', args=(self.object.id,))

'''
def delete_album(request, album_id):
    album = get_object_or_404(Post, pk=album_id)

    if request.method == "POST":
        album.delete()
        return HttpResponseRedirect(reverse('albuns:index'))

    context = {'album': album}
    return render(request, 'albuns/delete.html', context)
    '''

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'albuns/delete.html'
    context_object_name = 'album'
    success_url = reverse_lazy('albuns:index')