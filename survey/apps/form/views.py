from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request,'form/index.html')

def process(request):
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 1

    request.session['name'] = request.POST['name']
    request.session['dojo'] = request.POST['dojo_location']
    request.session['language'] = request.POST['favorite_language']
    request.session['comment'] = request.POST['comments']
    return redirect('/result')

def result(request):
    return render(request, 'form/result.html')