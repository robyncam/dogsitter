from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from .forms import RegisterForm, ProfileForm, LoginForm, DogForm
from django.contrib.auth.decorators import login_required
from . import models


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
            return redirect('home')
        else:
            messages.info(request, "Credientials do not match, try again")
            return redirect('login')

    context = {"form": form}
    return render(request, 'login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('home')


@login_required
def profile(request):
    form = ProfileForm()
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            new_profile = form.save(commit=False)
            new_profile.user = request.user
            new_profile.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'profile.html', context)


#
@login_required
def edit_profile(request):
    current_user = request.user
    profile = models.Profile.objects.get(user_id=current_user.id)
    form = ProfileForm(instance=profile)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            return redirect('profile_page')

    context = {'form': form}
    return render(request, 'edit_profile.html', context)


@login_required
def profilepage(request):
    context = {'profile': request.user.profile}
    return render(request, 'profilepage.html', context)


@login_required
def add_dog(request):
    form = DogForm()
    if request.method == "POST":
        form = DogForm(request.POST)
        if form.is_valid():
            dog_profile = form.save(commit=False)
            dog_profile.user = request.user
            dog_profile.save()
            return redirect('profile_page')

    context ={'form':form}
    return render(request, "add_dog.html", context)