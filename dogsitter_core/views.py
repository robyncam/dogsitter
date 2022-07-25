from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import auth, User
from django.contrib import messages
from .forms import RegisterForm, ProfileForm, LoginForm, DogForm
from django.contrib.auth.decorators import login_required
from . import models
from .models import Profile
from itertools import chain



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
            messages.info(request, "Credentials do not match, try again")
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
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            new_profile = form.save(commit=False)
            new_profile.user = request.user
            new_profile.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'profile.html', context)


@login_required
def edit_profile(request):
    current_user = request.user
    profile = models.Profile.objects.get(user_id=current_user.id)
    form = ProfileForm(instance=profile)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
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
            dog = form.save(commit=False)
            dog.user = request.user
            dog.save()
            return redirect('profile_page')

    context = {'form': form}
    return render(request, "add_dog.html", context)


def dog_profile(request, dog_pk):
    dog = get_object_or_404(models.Dog, pk=dog_pk)
    context = {'dog': dog}
    return render(request, 'dog_profile.html', context)


def search_results(request):
    if request.method == "POST":
        searched_location = request.POST['searched_location']
        searched_name = request.POST['searched_name']
        searched_locations = User.objects.filter(profile__location__contains=searched_location)
        searched_names = User.objects.filter(first_name__contains=searched_name)

        context = {'searched_names': searched_names, 'searched_name':searched_name, 'searched_locations':searched_locations, 'searched_location':searched_location}
        return render(request, 'search_results.html', context)
    else:
        return render(request, 'search_results.html')

