from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import auth
from django.contrib import messages
from .forms import RegisterForm, ProfileForm, LoginForm, DogForm, GalleryImageForm
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
            return redirect('profile_page', profile.pk)

    context = {'form': form, 'profile': profile}
    return render(request, 'edit_profile.html', context)


@login_required
def profilepage(request, profile_pk):
    profile = get_object_or_404(models.Profile, pk=profile_pk)
    context = {'profile': profile}
    return render(request, 'profilepage.html', context)


@login_required
def add_dog(request):
    current_user = request.user
    profile = models.Profile.objects.get(user_id=current_user.id)
    form = DogForm()
    if request.method == "POST":
        form = DogForm(request.POST)
        if form.is_valid():
            dog = form.save(commit=False)
            dog.user = request.user
            dog.save()
            return redirect('profile_page', profile.pk)

    context = {'form': form, 'profile': profile}
    return render(request, "add_dog.html", context)


def dog_profile(request, dog_pk):
    dog = get_object_or_404(models.Dog, pk=dog_pk)
    context = {'dog': dog}
    return render(request, 'dog_profile.html', context)


@login_required
def add_images(request):
    current_user = request.user
    profile = models.Profile.objects.get(user_id=current_user.id)
    form = GalleryImageForm()
    if request.method == "POST":
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            images = request.FILES.getlist('image')
            for image in images:
                models.GalleryImage.objects.create(image=image, user=request.user)
            return redirect('profile_page', profile.pk)

    context = {'form': form, 'profile': profile}
    return render(request, 'add_images.html', context)


def view_gallery(request, profile_pk):
    profile = get_object_or_404(models.Profile, pk=profile_pk)
    current_user = request.user
    context = {'profile': profile, "current_user": current_user}
    return render(request, 'view_gallery.html', context)


def update_info(request):
    current_user = request.user
    user = models.User.objects.get(user_id=current_user.id)
    form = RegisterForm(instance=user)
    if request.method == "POST":
        form = RegisterForm(request.POST, instance=user)
        if form.is_valid():
            user = user.save(commit=False)
            user.save()
            return redirect('profile_page', profile.pk)

    context = {'form': form, 'user': user}
    return render(request, "update_info.html", context)