from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import RegisterForm, ProfileForm, LoginForm

# Create your views here.

def home(request):
    return render(request, 'home.html')


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('home')


    context = {'form': form}
    return render(request, 'register.html', context)

def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)

        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Credientials do not match, try again")
            return redirect('login')

    context = {"form": form}
    return render(request, 'login.html', context)


def profile(request):
    form = ProfileForm()
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'profile.html', context)

