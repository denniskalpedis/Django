from django.shortcuts import render, redirect, HttpResponse
from models import Users, Courses
def index(request):
    if 'id' not in request.session:
        return redirect('/')
    context = {
        'user': Users.objects.get(id=request.session['id']),
        'courses': Courses.objects.all()
    }
    return render(request, 'courses/index.html', context)

def new(request):
    if request.method == 'POST':
        errors = Courses.objects.validate(request.POST)
        if len(errors):
            for error in errors:
                messages.error(request, error)
            return redirect('/courses')
        name = request.POST['name']
        desc = request.POST['desc']
        user = Users.objects.get(id=request.session['id'])
        Courses.objects.create(name=name,desc=desc,creator=user)
    return redirect('/courses')

def join(request, id):
    if 'id' not in request.session:
        return redirect('/')
    user = Users.objects.get(id= request.session['id'])
    course = Courses.objects.get(id=id)
    user.courses.add(course)
    return redirect('/courses')

def drop(request, id):
    if 'id' not in request.session:
        return redirect('/')
    user = Users.objects.get(id= request.session['id'])
    course = Courses.objects.get(id=id)
    user.courses.remove(course)
    course.attendees.remove(user)
    return redirect('/courses')

def edit(request, id):
    if 'id' not in request.session:
        return redirect('/')
    context = {
        'course': Courses.objects.get(id=id)
    }
    return render(request, 'courses/edit.html', context)

def delete(request, id):
    if 'id' not in request.session:
        return redirect('/')
    course = Courses.objects.get(id=id)
    if request.session['id'] != course.creator.id:
        return redirect('/courses')

    course.delete()
    return redirect('/courses')

def confirm(request, id):
    if 'id' not in request.session:
        return redirect('/')
    course = Courses.objects.get(id=id)
    if request.session['id'] != course.creator.id:
        return redirect('/courses')
    context = {
        'course': course
    }
    return render (request, 'courses/delete.html', context)
    

def update(request, id):
    if 'id' not in request.session:
        return redirect('/')
    course = Courses.objects.get(id=id)
    if request.session['id'] != course.creator.id:
        return redirect('/courses')
    if request.method == 'POST':
        errors = Courses.objects.validate(request.POST)
        if len(errors):
            for error in errors:
                messages.error(request, error)
            return redirect('/courses')
    course.name = request.POST['name']
    course.desc = request.POST['desc']
    course.save()
    return redirect('/courses')

    
