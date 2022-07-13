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
    current_year = int(date.today().year)
    YEAR_CHOICES = list(range(current_year, (current_year - 25), -1))
    dob = forms.DateField(label="Date of Birth: ", widget=forms.SelectDateWidget(years=YEAR_CHOICES))

    class Meta:
        model = Dog

        labels = {
            'good_with_cats': 'Is your dog good with cats?',
            'good_with_kids': 'Is your dog good with kids?',
            'good_with_dogs': 'Is your dog good with other dogs?:',
            'bio': 'Tell us about your pup!:',
            'weight': "Weight (in pounds):",
        }

        fields = ['name', 'dob', 'weight', 'good_with_cats', 'good_with_kids', 'good_with_dogs', 'bio', 'dob']
