from django.shortcuts import render, HttpResponse, redirect
from models import Users
from django.contrib import messages
import bcrypt

def index(request):
    if 'id' in request.session:
        return redirect('/courses')
    return render(request, 'login/index.html')

def login(request):
    if request.method == "POST":
        errors = Users.objects.validation(request.POST)
        if len(errors):
                for error in errors:
                    messages.error(request, error)
                return redirect('/')
        current_user = Users.objects.get(email=request.POST['email'])
        request.session['id'] = current_user.id
        return redirect('/courses')
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
        return redirect('/courses')
    else:
        return redirect('/')

def logout(request):
    if 'id' in request.session:
        del request.session['id']
    return redirect('/')    


