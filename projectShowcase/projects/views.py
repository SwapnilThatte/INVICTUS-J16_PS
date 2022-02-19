from django.shortcuts import redirect, render, HttpResponse
from projects.models import Projects  
from django.contrib.auth.models import User, auth
# Create your views here.

def home(request):
    return render(request, 'home.html')

def projects(request):
    project = Projects.objects.all()
    context = {'projects': project}
    print(f"\n\n\n{project}\n\n\n")
    return render(request, 'projects.html', context)


def newproject(request):

    return render(request, 'newproject.html')

def register(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
       
        user = User.objects.create_user(username=name, email=email, password=password)
        user.save()
        print('\n\n\n USER CREATED \n\n\n')
        return redirect('/')
        
    else:
        pass


    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')

