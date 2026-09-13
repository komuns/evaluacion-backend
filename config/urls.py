from django.contrib import admin
from django.urls import path


from app1 import views as app1_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    
    path('vista1/', app1_views.vista_uno, name='vista1'),
    path('vista2/', app1_views.vista_dos, name='vista2'),
]