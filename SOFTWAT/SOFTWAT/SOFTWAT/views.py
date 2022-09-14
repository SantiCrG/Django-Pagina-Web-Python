from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib import messages

#para enviar emails y que las funciones sirvan en views
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

def paginaprincipal(request):
    return render(request,'PAGINA_PRINCIPAL.HTML',{
        #context
    })

def ClienteInicio(request):
    return render(request,'cliente_inicio.html',{
        #context
    })

def Mision(request):
    return render(request,'Mision.html',{
        #context
    })

def CatPinturas(request):
    return render(request,'PINTURAS.HTML',{
        #context
    })

def CatRollos(request):
    return render(request,'ROYOS.HTML',{
        #context
    })

def Aplicacion(request):
    return render(request,'APLICACION.HTML',{
        #context
    })

def Domicilio(request):
    return render(request,'Seleccione.html',{
        #context
    })

def Carrito(request):
    return render(request,'VENTAS.HTML',{
        #context
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('admin:index')
        else: 
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'login.html',{

    })

def PQRS(request):
    return render(request,'PQRS.html',{
     #context
    })

#funcion para renderisar las funciones del email
def PQRS(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        template = render_to_string('email_template.html', {
            'name': name,
            'email': email,
            'message': message
        })
    #consolidacion de nuestro correo electronico
    #nos va a trar subject y luego lo que hay en email_TEMPLATE
    # y la configuracion de settings.email_host_user que hay que implementar
        email = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            ['holman10025@gmail.com']
        )
    
        email.fail_silently = False
        email.send()
    
    return render(request, 'PQRS.html',{

    })