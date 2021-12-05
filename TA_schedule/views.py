from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render, redirect
from django.views import View
from .UserFactory import UserFactory
from .forms import UserUpdateForm, PersonalInfoUpdateForm, CourseCreateForm, LabCreateForm
from django.core.exceptions import ObjectDoesNotExist

from .models import PersonalInfo, Class, Lab, ClassToLab


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    try:
        instance.personalinfo.save()
    except ObjectDoesNotExist:
        PersonalInfo.objects.create(user=instance)


class Home(View):
    def get(self, request):
        return render(request, "home.html")

    def post(self, request):
        return render(request, "login.html")


class DashBoard(View):
    def get(self, request):
        return render(request, "dashboard.html")

    def post(self, request):
        return render(request, "dashboard.html")


class CourseAdd(View):
    def get(self, request):
        c_form = CourseCreateForm()
        l_form = LabCreateForm()

        context = {
            'c_form': c_form,
            'l_form': l_form
        }
        return render(request, "addcourse.html", context)

    def post(self, request):
        c_form = CourseCreateForm(request.POST)
        l_form = LabCreateForm(request.POST)

        if c_form.is_valid() and l_form.is_valid():
            c_form.save()
            l_form.save()
            c = list(Class.objects.filter(name=c_form.cleaned_data.get('name')))
            lab = list(Lab.objects.filter(section=l_form.cleaned_data.get('section')))
            ClassToLab.objects.create(class_id=c.pop(), lab_id=lab.pop())
            messages.success(request, f'Your class has been added!')
            return redirect('/courses/')
        # else:
        #     return redirect('/dashboard/')
        context = {
            'c_form': c_form,
            'l_form': l_form
        }
        return render(request, "addcourse.html", context)


class Courses(View):

    def get(self, request):
        course_lab_list = []

        course_list = list(Class.objects.all())
        for i in course_list:
            class_lab_list = list(ClassToLab.objects.filter(class_id=i))
            lab_list = []
            ta_name = []
            for j in class_lab_list:
                lab_list.append(j.lab_id.section)
                ta_name.append(j.lab_id.ta_name)
            course_lab_list.append((i, lab_list, ta_name))
        # lab_list = ClassToLab.objects.filter()
        return render(request, "courses.html", {"courses": course_lab_list})

    def post(self, request):
        return render(request, "courses.html")


class Profile(View):

    def get(self, request):
        u_form = UserUpdateForm(instance=request.user)
        p_form = PersonalInfoUpdateForm(instance=request.user.personalinfo)

        context = {
            'u_form': u_form,
            'p_form': p_form
        }
        return render(request, "profile.html", context)
        # return render(request, "profile.html")

    def post(self, request):
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = PersonalInfoUpdateForm(request.POST, instance=request.user.personalinfo)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('/dashboard/')
        context = {
            'u_form': u_form,
            'p_form': p_form
        }
        return render(request, "profile.html", context)
