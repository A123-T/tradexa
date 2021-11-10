from django.shortcuts import redirect, render,HttpResponseRedirect
from .forms import SignUpForm,modify_post1
from django.contrib import messages
from .models import post
import datetime
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def abhay(request):
    if request.user.is_authenticated:
        return render(request,'home.html')
    else:
        return redirect('/alogin/')


def user_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    if request.method == "POST":
        fm = AuthenticationForm(request=request ,data = request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            print(uname,upass)
            user = authenticate(username = uname, password =upass )
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/')
        else:
            messages.success(request,'you are not a valid user register first')
            return  HttpResponseRedirect('/register/')
    else:
        fm = AuthenticationForm()
    return render(request,'login.html',{'form':fm,'nam':'LOGIN FORM'})

def register(request):
    if request.method == "POST":
        ab = SignUpForm(request.POST)
        if ab.is_valid():
            messages.success(request,'CONGRATULATIONS YOUR ACCOUNT HAS BEEN SUCCCEFULLY CREATED ')
            ab.save()
            return HttpResponseRedirect('/')
    else:
        ab = SignUpForm() 
    return  render(request,'signup.html',{'form':ab})

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/alogin/')
    else:
        messages.success(request,'First login the page !!')
        return HttpResponseRedirect('/')

def post_print(request):
    if request.user.is_authenticated:
        ab = post.objects.all().filter()
        return render(request,'show_post.html',{'post_value':ab})
    else:
        return HttpResponseRedirect('/alogin/')

def update_post(request):
    if request.user.is_authenticated:
        ab = post.objects.all()
        return render(request,'modify_post.html',{'post_value':ab}) 
    else:
        return HttpResponseRedirect('/alogin/')

def modify_post(request,id1):
    if request.user.is_authenticated:
        if request.method == "POST":
            bc = request.POST.get('abc')
            print(bc)
            ab = post.objects.get(id = id1)
            ab.text = bc 
            ab.updated_at = datetime.datetime.now()
            ab.save()
            messages.success(request,'YOU HAVE SUCCESSUFULLY UPDATED THE POST')
            return HttpResponseRedirect('/post/')
        else:
            ab = post.objects.get(id = id1)
            return render(request,"modify_post.html",{'pos':ab,'nam':'Modefied Post'})
    else:
        return HttpResponseRedirect('/alogin/')


def create_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            ab = modify_post1(request.POST)
            if ab.is_valid():
                bc = post(user = request.user,text = ab.cleaned_data['text'],created_at = datetime.datetime.now(),updated_at = datetime.datetime.now())
                bc.save()
                messages.success(request,'POST UPDATED SUCCESSFULLY ')
                return HttpResponseRedirect('/post/')
        else:
            ab = modify_post1()
            return render(request,'login.html',{'form':ab,'nam':'CREATE POST'})
    else:
        return HttpResponseRedirect('/alogin/')

        

