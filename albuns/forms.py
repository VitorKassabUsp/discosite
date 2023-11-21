from django import forms


from django.forms import ModelForm
from .models import Post, Comment


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'release_year',
            'poster_url',
            'content',
            'band',

        ]
        labels = {
            'title': 'Título',
            'release_year': 'Data de Lançamento',
            'poster_url': 'URL do Poster',
            'content': 'Descrição',
            'band': 'Artista',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'author',
            'text',
        ]
        labels = {
            'author': 'Usuário',
            'text': 'Comentário',
        }