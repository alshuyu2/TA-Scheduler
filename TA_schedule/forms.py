from django import forms
from django.contrib.auth.models import User
from .models import PersonalInfo, Class, Lab


# class My_Form(forms.ModelForm):
#     class Meta:
#         model = My_Class
#         fields = ('first_name', 'last_name' , 'address')
#
#     def __init__(self, *args, **kwargs):
#         super(My_Form, self).__init__(*args, **kwargs)
#         self.fields['address'].required = False

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class   PersonalInfoUpdateForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = ['office_hours', 'phone']


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['name', 'instr_id']

    def clean(self):
        cleaned_data = self.cleaned_data
        name = cleaned_data.get('name')

        try:
            course = Class.objects.get(name=name)
        except Class.DoesNotExist:
            course = None

        if course:
            msg = u"Course name: %s already exists." % name
            self._errors['name'] = self.error_class([msg])
            del cleaned_data['name']
            return cleaned_data
        else:
            return self.cleaned_data


class LabCreateForm(forms.ModelForm):
    class Meta:
        model = Lab
        fields = ['section', 'ta_name']


class UserCreateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class PersonalInfoCreateForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = ['office_hours', 'phone', 'role']
