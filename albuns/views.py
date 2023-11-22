from django.shortcuts import render

from django.http import HttpResponse
from .temp_data import album_data
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls import reverse_lazy
from .models import Post, Comment, Category
from .forms import PostForm, CommentForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class PostListView(ListView):
    model = Post
    template_name = 'albuns/index.html'
    context_object_name = 'album_list'


class PostDetailView(DetailView):
    model = Post
    template_name = 'albuns/detail.html'
    context_object_name = 'album'
    pk_url_kwarg = 'album_id'


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
        

class PostCreateView(CreateView): 
    model = Post
    form_class = PostForm
    template_name = 'albuns/create.html'
    success_url = reverse_lazy('albuns:create')

    def form_valid(self, form):
        response = super().form_valid(form)
        # Após criar o post, redirecione para os detalhes do post recém-criado
        return HttpResponseRedirect(reverse('albuns:detail', args=(self.object.id,)))


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'albuns/update.html'
    context_object_name = 'album'

    def get_success_url(self):
        return reverse_lazy('albuns:detail', args=(self.object.id,))


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'albuns/delete.html'
    context_object_name = 'album'
    success_url = reverse_lazy('albuns:index')

def create_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_author = form.cleaned_data['author']
            comment_text = form.cleaned_data['text']
            comment = Comment(author=comment_author,
                            text=comment_text,
                            post=post)
            comment.save()
            return HttpResponseRedirect(
                reverse('albuns:detail', args=(post_id, )))
    else:
        form = CommentForm()
    context = {'form': form, 'post': post}
    #return HttpResponseRedirect(reverse('albuns:detail', args=(post_id,)))
    return render(request, 'albuns/comment.html', context)


class CategoryListView(generic.ListView):
    model = Category
    template_name = 'albuns/category.html'
    context_object_name = 'category_list'

class CategoryPostsListView(generic.ListView):
    template_name = 'albuns/index.html'
    context_object_name = 'post_list'

    def get_category(self):
        return Category.objects.get(pk=self.kwargs['category_id'])

    def get_queryset(self):
        return self.get_category().posts.all()
    
    def get_context_data(self, **kwargs):
        category = self.get_category()
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Categoria'
        context['albumpage_title'] = f'Categoria {category.name}'
        context['category'] = True
        context['category_id'] = category.id
        return context