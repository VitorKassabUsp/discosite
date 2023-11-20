from django.contrib import admin
from django.urls import include, path # modificar esta linha

urlpatterns = [
    path('staticpages/', include('staticpages.urls')), # adicionar esta linha
    path('admin/', admin.site.urls),
]
