from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.urls import reverse

from .forms import SignUpForm,ProfileForm
from .models import Profile


# MESSAGES
from django.contrib import messages


from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
# Create your views here.

def signup(request):
    form = SignUpForm
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'ACCOUNT CREATED SUCCESSFULLY!')
            return HttpResponseRedirect(reverse('loginapp:login'))

    dict= {'form':form}
    return render(request,'loginapp/signup.html',dict)        

def login_page(request):
    form = AuthenticationForm
    if request.method =='POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('shop:home'))
               

    dict = {'form':form}
    return render(request,'loginapp/login.html',dict)     

@login_required
def logout_page(request):
    logout(request)
    messages.warning(request,'YOU ARE LOGGED OUT!')
    return HttpResponseRedirect(reverse('shop:home'))

@login_required
def user_profile(request):
    profile = Profile.objects.get(user=request.user)

    form = ProfileForm(instance=profile)
    if request.method =='POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request,'PROFILE UPDATED SUCCESSFULLY!')

            form = ProfileForm(instance=profile)

    dict = {'form':form}
    return render(request,'loginapp/change_profile.html',dict)        






