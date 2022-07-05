from django.contrib import admin
from django.urls import path
from App import views



urlpatterns = [
    #path para acceder al ADMIN SITE
    path('admin/', admin.site.urls),
    
    #path para el render de la homepage
    path('', views.home, name="home"),

    #path para el render de las ofertas laborales
    path('ofertas', views.ofertas, name="ofertas"),

    #path para enviar el form frontend
    path('email_frontend', views.email_frontend, name="email_frontend"),

    #path para enviar el form backend
    path('email_backend', views.email_backend, name="email_backend"),

    #path para enviar el form ciberseguridad
    path('email_ciberseguridad', views.email_ciberseguridad, name="email_ciberseguridad"),

]
