from django import forms
from django.contrib.auth.models import User
from .models import Profile, Dog
from datetime import date


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
    BOOL_CHOICES = [(True, 'Yes'), (False, 'No')]
    BREEDS = [('boxer', 'Boxer'), ('golden', 'Golden'), ('bulldog', 'Bulldog')]
    current_year = int(date.today().year)
    YEAR_CHOICES = range(current_year, (current_year - 25), -1)
    dob = forms.DateField(label="Date of Birth: ",
                          widget=forms.SelectDateWidget(years=YEAR_CHOICES))
    good_with_cats = forms .CharField(label='Is your dog good with cats?',
                                      widget=forms.RadioSelect(choices=BOOL_CHOICES))
    good_with_kids = forms.CharField(label='Is your dog good with kids?',
                                     widget=forms.RadioSelect(choices=BOOL_CHOICES))
    good_with_dogs = forms.CharField(label='Is your dog good with other dogs?',
                                     widget=forms.RadioSelect(choices=BOOL_CHOICES))

    class Meta:
        model = Dog
        labels = {
            'bio': 'Tell us about your pup!:',
            'weight': "Weight (in pounds):",
            'breed': "What breed is your dog?:",
        }

        fields = ['name', 'dob', 'weight', 'good_with_cats',
                  'good_with_kids', 'good_with_dogs', 'bio', 'dob', 'breed']
