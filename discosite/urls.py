from django.contrib import admin
from django.urls import include, path # modificar esta linha

urlpatterns = [
    path('', include('staticpages.urls')),
    path('admin/', admin.site.urls),
]
