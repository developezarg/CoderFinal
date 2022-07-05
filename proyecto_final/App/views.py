from email import message
from multiprocessing import context
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template import loader
from App.models import Registro_email

#función para acceder a la homepage
def home(request):
    return render(request, "home.html")


#función para acceder a las ofertas laborales
def ofertas(request):
    return render(request, "ofertas.html")


#funcion para enviar el form frontend
def email_frontend (request):
    if request.method == "POST":

#Chequeo de preexistencia de email en la BBDD
        email = request.POST["email"]
        if Registro_email.objects.filter(email=email).exists():
            messages.error(request, "Ya tenemos tu CV en nuestra BBDD") 
            return HttpResponseRedirect("/ofertas")
        #_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_     
        else:
            nombre = request.POST.get("nombre")
            edad = request.POST.get("edad")
            telefono = request.POST.get("telefono")
            email = request.POST.get("email")
            Personal = request.POST.get("Personal")
            Experiencia = request.POST.get("Experiencia")

            #registro en la BBDD
            contact = Registro_email
            contact.email = email
            contact.save()
            #_-_-_-_-_-_-_-_-_-_-_-_

            template=loader.get_template("CV_form.txt")
            context= {
                "nombre" : nombre,
                "edad" : edad, 
                "telefono" : telefono,
                "email" : email,
                "Personal" : Personal,
                "Experiencia" : Experiencia,
                       
            }
            message=template.render(context)
            email=EmailMultiAlternatives("Candidat@-Frontend", message, "Oferta Frontend", ["withetower.rrhh@gmail.com", email])
            email.content_subtype = "html"
            file = request.FILES["archivo"]
            email.attach(file.name, file.read, file.content, file.content.type)
            email.send()
            email.success(request, "CV de Frontend enviado satisfactoriamente !")
            return HttpResponseRedirect("/")

#funcion para enviar el form backend
def email_backend (request):
    if request.method == "POST":
            nombre = request.POST.get("nombre")
            edad = request.POST.get("edad")
            telefono = request.POST.get("telefono")
            email = request.POST.get("email")
            Personal = request.POST.get("Personal")
            Experiencia = request.POST.get("Experiencia")
            
            template=loader.get_template("CV_form.txt")
            context= {
                "nombre" : nombre,
                "edad" : edad,
                "telefono" : telefono,
                "email" : email,
                "Personal" : Personal,
                "Experiencia" : Experiencia,
                       
            }
            message=template.render(context)
            email=EmailMultiAlternatives("Candidat@-Backend", message, "Oferta Backend", ["withetower.rrhh@gmail.com", email])
            email.content_subtype = "html"
            file = request.FILES["archivo"]
            email.attach(file.name, file.read, file.content, file.content.type)
            email.send()
            email.success(request, "CV de Frontend enviado satisfactoriamente !")
            return HttpResponseRedirect("/")

#funcion para enviar el form ciberseguridad
def email_ciberseguridad (request):
    if request.method == "POST":
            nombre = request.POST.get("nombre")
            edad = request.POST.get("edad")
            telefono = request.POST.get("telefono")
            email = request.POST.get("email")
            Personal = request.POST.get("Personal")
            Experiencia = request.POST.get("Experiencia")
            
            template=loader.get_template("CV_form.txt")
            context= {
                "nombre" : nombre,
                "edad" : edad,
                "telefono" : telefono,
                "email" : email,
                "Personal" : Personal,
                "Experiencia" : Experiencia,
                       
            }
            message=template.render(context)
            email=EmailMultiAlternatives("Candidat@-Ciberseguridad", message, "Oferta Ciberseguridad", ["withetower.rrhh@gmail.com", email])
            email.content_subtype = "html"
            file = request.FILES["archivo"]
            email.attach(file.name, file.read, file.content, file.content.type)
            email.send()
            email.success(request, "CV de Ciberseguridad enviado satisfactoriamente !")
            return HttpResponseRedirect("/")


