from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PersonalInfo, Class, Lab, TAtoClass


# class My_Form(forms.ModelForm):
#     class Meta:
#         model = My_Class
#         fields = ('first_name', 'last_name' , 'address')
#
#     def __init__(self, *args, **kwargs):
#         super(My_Form, self).__init__(*args, **kwargs)
#         self.fields['address'].required = False
from .roles import Role


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class PersonalInfoUpdateForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = ['office_hours', 'phone']


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['name', 'instr_id']

    def clean(self):
        cleaned_data = self.cleaned_dataf
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

    def __init__(self, *args, **kwargs):
        super(LabCreateForm, self).__init__(*args, **kwargs)
        self.fields['section'].required = False
        self.fields['ta_name'].required = False


class UserCreateForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class PersonalInfoCreateForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = ['office_hours', 'phone', 'role']


class TAtoCourseAddForm(forms.ModelForm):
    class Meta:
        model = TAtoClass
        fields = ['class_name', 'ta_name']


    def __init__(self, *args, **kwargs):
        super(TAtoCourseAddForm, self).__init__(*args, **kwargs)
        self.fields['ta_name'].queryset = User.objects.filter(personalinfo__role=Role.TA)
        # self.fields['class_name'].widget.attrs['style'] = 'width:400px; height:40px;'
        # self.fields['ta_name'].widget.attrs['style'] = 'width:400px; height:40px;'


class SkillsUpdateForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = ['skills']
