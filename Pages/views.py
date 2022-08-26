from django.shortcuts import render, redirect 
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import *
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, Email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('actualite')
        else:
            messages.success(request, ("try again"))
            return redirect('index')
    else:
        return render(request,'user/index.html', {})


def inscription(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        data = Compte(username=username, Email=email,password=password)
        data.save()

    return render(request,'user/inscription.html')

def about(request):
    return render(request,'user/apropos.html')

def contact(request):
    return render(request,'user/contact.html')

def actualite(request):
    return render(request,'user/actualite.html',{"act":Post.objects.all()})

def reservation(request):
    return render(request,'user/reservation.html',{"res":resSport.objects.all(), "res2":resRestauration.objects.all()})

def reservation1(request):
        submitted = False
        if request.method == "POST":
            form = Restauration(request.POST)
            if form.is_valid():
               form.save()
            return HttpResponseRedirect('?submitted=True')
        else:
            form =Restauration
            if 'submitted' in request.GET:
                submitted = True

        return render(request,'user/reservation1.html', {'form':form, 'submitted':submitted})

def reservation2(request):
        submitted = False
        if request.method == "POST":
            form = Sport(request.POST)
            if form.is_valid():
               form.save()
            return HttpResponseRedirect('?submitted=True')
        else:
            form =Sport
            if 'submitted' in request.GET:
                submitted = True

        return render(request,'user/reservation2.html', {'form':form, 'submitted':submitted})

###########################
def actualite2(request):
    return render(request,'admin/actualite2.html',{"act":Post.objects.all()})

def admin1(request):
    return render(request,'admin/admin1.html',{"res":resSport.objects.all(), "res2":resRestauration.objects.all()})

def more1(request):
    return render(request,'admin/more1.html', {"res2":resRestauration.objects.all()})

def more2(request):
    return render(request,'admin/more2.html',{"res":resSport.objects.all()})

def post(request):
    submitted = False
    if request.method == "POST":
        form = Opost(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form =Opost
        if 'submitted' in request.GET:
            submitted = True

    return render(request,'admin/post.html', {'form':form, 'submitted':submitted}) 