from django import forms
from django.contrib.auth.models import User
from .models import Profile, Dog


class RegisterForm(forms.ModelForm):
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password'] != cleaned_data['confirm_password']:
            raise forms.ValidationError({"confirm_password": "Passwords do not match"})

        return cleaned_data


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        labels = {
            'location': 'Where are you located?',
            'cost': 'How much do you charge per day?',
            'is_dog_sitter': 'Are you a dog sitter?',
            'bio': 'Tell us a bit about yourself',
        }

        fields = ['location', 'cost', 'is_dog_sitter', 'bio']


class LoginForm(forms.ModelForm):
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username']

class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        labels = {
            'dob': 'Date of birth:',
            'good_with_cats': 'Are they good with cats?',
            'good_with_kids': 'Are they good with kids?',
            'bio': 'Tell us about your pup!:',
            'weight': "Weight (in pounds):",
        }

        fields = ['name', 'dob', 'weight', 'good_with_cats', 'good_with_kids']

    user = models.ForeignKey(User, models.CASCADE)
    name = models.CharField(max_length=200)
    dob = models.DateField()
    weight = models.DecimalField(decimal_places=2, max_digits=7)
    good_with_cats = models.BooleanField(default=None)
    good_with_kids = models.BooleanField(default=None)
    bio = models.TextField(max_length=100000)
