from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    designation = forms.CharField(max_length=100, required=True, help_text='Required.')
    institution = forms.CharField(max_length=100, required=True, help_text='Required.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','institution', 'designation', 'email', 'password1', 'password2', )

class CurriculumForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Curriculum Title"
        })
    )
    description = forms.CharField(
        max_length=1000,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Curriculum Description"
        })
    )

class BitForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Bit Title"
        })
    )

    bit_type = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Bit Type"
        })
    )

    description = forms.CharField(
        max_length=1000,
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Bit Description"
        })
    )

    file = forms.FileField(
        required=False
    )

    text = forms.CharField(
        max_length=1000,
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Text Content"
        })
    )

class ProfileForm(forms.Form):
    full_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Full name"
        })
    )

    email = forms.EmailField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Email"
        })
    )

    institution = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Institution"
        })
    )

    designation = forms.CharField(
        max_length=1000,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Designation"
        })
    )

    image = forms.FileField(
        required=False
    )