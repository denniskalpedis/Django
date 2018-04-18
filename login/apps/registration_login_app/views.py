from django.shortcuts import render, HttpResponse, redirect
from models import Users
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, 'registration_login_app/index.html')

def login(request):
    if request.method == "POST":
        errors = Users.objects.validation(request.POST)
        if len(errors):
                for error in errors:
                    messages.error(request, error)
                return redirect('/')
        current_user = Users.objects.get(email=request.POST['email'])
        request.session['id'] = current_user.id
        return redirect('/success')
    else:
        return redirect('/')   

def register(request):
    if request.method == "POST":
        errors = Users.objects.reg_validation(request.POST)
        if len(errors):
                for error in errors:
                    messages.error(request, error)
                return redirect('/')

        password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        f_name = request.POST['f_name'] 
        l_name = request.POST['l_name']
        email = request.POST['email']
        Users.objects.create(first_name=f_name,last_name=l_name,email=email,password=password)
        id = Users.objects.last()
        request.session['id'] = id.id
        return redirect('/success')
    else:
        return redirect('/')

def success(request):
    if 'id'  not in request.session:
        return redirect('/')
    context = {
        'users': Users.objects.all()
    }
    return render(request, 'registration_login_app/success.html', context)

