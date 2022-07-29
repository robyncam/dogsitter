from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='profile'),
    path('profile-page', views.profilepage, name='profile_page'),
    path('edit-profile', views.edit_profile, name='edit_profile'),
    path('add-images', views.add_images, name='add_images'),
    path('add-dog', views.add_dog, name='add_dog'),
    path('dog-profile/<int:dog_pk>', views.dog_profile, name='dog_profile'),
    path('view-gallery', views.view_gallery, name='view_gallery'),
    path('edit-dog/<int:dog_pk>', views.edit_dog, name='edit_dog'),
    path('add-dog-images/<int:dog_pk>', views.add_dog_images, name='add_dog_images'),
    path('view-dog-gallery/<int:dog_pk>', views.view_dog_gallery, name='view_dog_gallery'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
