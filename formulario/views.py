#from django.shortcuts import render
#from .models import Contacto


from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages

# Estas en las vistas de la APP: Formulario

def ver_contacto(request):
    return render(request, 'contacto.html')

def enviar_mail (request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        template = render_to_string('email.html', {
            'name' : name,
            'email' : email,
            'subject' : subject,
            'message' : message
        })

        emailSender = EmailMessage(
            subject, 
            template,
            settings.EMAIL_HOST_USER,
            ["delvallegodoyfernanda@gmail.com" ]

        )

        emailSender.content_subtype = 'html'
        emailSender.fail_silently = False
        emailSender.send()
        messages.success(request, 'El correo fue enviado exitosamente')
        return redirect('contacto')
