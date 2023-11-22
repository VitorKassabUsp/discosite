from django.urls import path

from . import views
from .views import PostDetailView, PostListView,  PostSearchView, PostCreateView, PostUpdateView,PostDeleteView, PostDetailView



app_name = 'albuns'
urlpatterns = [
    #path('', views.list_albuns, name='index'),
    path('albuns/', PostListView.as_view(), name='index'),

    #path('search/', views.search_albuns, name='search'),
    path('albuns/search/', PostSearchView.as_view(), name='search'),

    #path('create/', views.create_album, name='create'),
    path('albuns/create/', PostCreateView.as_view(), name='create'),

    #path('<int:album_id>/', views.detail_album, name='detail'),
    path('albuns/<int:album_id>/', PostDetailView.as_view(), name='detail'),
    
    #path('update/<int:album_id>/', views.update_album, name='update'),
    path('albuns/<int:pk>/update/', PostUpdateView.as_view(), name='update'),

    #path('delete/<int:album_id>/', views.delete_album, name='delete'),
    path('albuns/<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),

    path('albuns/<int:post_id>/comment/', views.create_comment, name='comment'),

    path('category/', views.CategoryListView.as_view(), name='category'),
    path('category-posts/<int:category_id>/', views.CategoryPostsListView.as_view(), name='category-posts'),
    path('albuns/category-post-detail/<int:category_id>/<int:pk>/', views.CategoryPostDetailView.as_view(), name='category-post-detail'),
    path('albuns/<int:album_id>/', views.PostDetailView.as_view(), name='detail'),
]
