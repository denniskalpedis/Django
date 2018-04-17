from django.shortcuts import render, HttpResponse, redirect
from models import Users
from django.contrib import messages

def index(request):
    context = {
        'users': Users.objects.all()
    }
    return render(request,'users_app/index.html', context)

def show(request, id):
    if request.method == "POST":
        f_name = request.POST['f_name'] 
        l_name = request.POST['l_name']
        email = request.POST['email']

        errors = Users.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/users/'+id+'/edit')

        entry = Users.objects.get(id=id)
        entry.first_name = f_name
        entry.last_name = l_name
        entry.email = email
        entry.save()

    context = {
        'user': Users.objects.get(id=id)
    }
    return render(request,'users_app/show.html', context)

def new(request):
    return render(request,'users_app/new.html')

def edit(request, id):
    context = {
        'user': Users.objects.get(id=id)
    }
    return render(request, 'users_app/edit.html', context)

def destroy(request, id):
    entry = Users.objects.get(id=id)
    entry.delete()
    return redirect('/users')

def create(request):
    f_name = request.POST['f_name'] 
    l_name = request.POST['l_name']
    email = request.POST['email']
    errors = Users.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/users/new')
    
    Users.objects.create(first_name=f_name,last_name=l_name,email=email)
    return redirect('/users')  