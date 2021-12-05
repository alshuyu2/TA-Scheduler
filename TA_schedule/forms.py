from django import forms
from django.contrib.auth.models import User
from .models import PersonalInfo


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class PersonalInfoUpdateForm(forms.ModelForm):

    class Meta:
        model = PersonalInfo
        fields = ['office_hours', 'phone']


class UserCreateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class PersonalInfoUpdateForm(forms.ModelForm):

    class Meta:
        model = PersonalInfo
        fields = ['office_hours', 'phone', 'role']

