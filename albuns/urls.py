from django.urls import path

from . import views

app_name = 'albuns'
urlpatterns = [
    path('', views.list_albuns, name='index'),
    path('search/', views.search_albuns, name='search'),
    path('create/', views.create_album, name='create'),
    path('<int:album_id>/', views.detail_album, name='detail'),
    path('update/<int:album_id>/', views.update_album, name='update'),
    path('delete/<int:album_id>/', views.delete_album, name='delete'),
]