from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='profile'),
    path('profile-page', views.profilepage, name='profile_page'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('add_images', views.add_images, name='add_images'),
    path('add_dog', views.add_dog, name='add_dog'),
    path('dog_profile/<int:dog_pk>', views.dog_profile, name='dog_profile'),

]
