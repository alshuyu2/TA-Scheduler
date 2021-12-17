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
        fields = ['office_hours', 'address', 'phone']


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

    def __init__(self, *args, **kwargs):
        super(CourseCreateForm, self).__init__(*args, **kwargs)
        self.fields['instr_id'].queryset = User.objects.filter(personalinfo__role=Role.INSTRUCTOR)


class LabCreateForm(forms.ModelForm):
    class Meta:
        model = Lab
        fields = ['section']

    def __init__(self, *args, **kwargs):
        super(LabCreateForm, self).__init__(*args, **kwargs)
        self.fields['section'].required = False
        # self.fields['ta_name'].required = False
        # self.fields['ta_name'].queryset = User.objects.filter(personalinfo__role=Role.TA)

    def clean(self):
        cleaned_data = self.cleaned_data
        name = cleaned_data.get('section')

        # try:
        #     lab = Lab.objects.get(section=name)
        # except Lab.DoesNotExist:
        #     lab = None

        if name == '':
            msg = 'Invalid lab form'
            self._errors['section'] = self.error_class([msg])
            del cleaned_data['section']
            return cleaned_data
        else:
            return self.cleaned_data


class UserCreateForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class PersonalInfoCreateForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = ['role', 'office_hours', 'phone', 'address']

    def __init__(self, *args, **kwargs):
        super(PersonalInfoCreateForm, self).__init__(*args, **kwargs)
        self.fields['office_hours'].required = False
        self.fields['phone'].required = False
        self.fields['address'].required = False


class TAtoCourseAddForm(forms.ModelForm):

    class Meta:
        model = TAtoClass
        fields = ['class_name', 'ta_name']

    def clean(self):
        cleaned_data = self.cleaned_data
        c_name = cleaned_data.get('class_name')
        ta_name = cleaned_data.get('ta_name')
        try:
            add = TAtoClass.objects.get(class_name=c_name, ta_name=ta_name)
        except TAtoClass.DoesNotExist:
            add = None

        if add:
            msg = f" {ta_name} already belongs to {c_name}."# % ta_name, c_name
            self._errors['ta_name'] = self.error_class([msg])
            self._errors['class_name'] = self.error_class([''])
            del cleaned_data['ta_name']
            del cleaned_data['class_name']
            return cleaned_data
        else:
            return self.cleaned_data

    def __init__(self, *args, **kwargs):
        super(TAtoCourseAddForm, self).__init__(*args, **kwargs)
        self.fields['ta_name'].queryset = User.objects.filter(personalinfo__role=Role.TA)
        # self.fields['class_name'].widget.attrs['style'] = 'width:400px; height:40px;'
        # self.fields['ta_name'].widget.attrs['style'] = 'width:400px; height:40px;'


class SkillsUpdateForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = ['skills']


class RemoveUserForm(forms.ModelForm):
    username = forms.ModelChoiceField(queryset=User.objects.all())
    class Meta:
        model = User
        # username = forms.ModelChoiceField(queryset=User.objects.all())
        fields = ['username']

        # widget=forms.Select(choices= User.objects.all())
    def clean(self):
        cleaned_data = self.cleaned_data
        name = cleaned_data.get('username')
        print (cleaned_data)

        try:
            users = User.objects.get(username=name)
        except User.DoesNotExist:
            users = None

        if not users:
            msg = u"Username : %s doesn't exists." % name
            self._errors['username'] = self.error_class([msg])
            del cleaned_data['username']
            return cleaned_data
        else:
            return self.cleaned_data
