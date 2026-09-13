from django.contrib import admin
from django.urls import path


from app2 import views as app2_views


urlpatterns = [
    path('admin/', admin.site.urls),
    
    
    path('vista3/', app2_views.vista_tres, name='vista3'),
    path('vista4/', app2_views.vista_cuatro, name='vista4'),
    
    
]