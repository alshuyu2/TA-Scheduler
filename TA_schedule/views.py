from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render, redirect
from django.views import View
from MyClasses.Lab import Lab
from .forms import UserUpdateForm, PersonalInfoUpdateForm
from django.core.exceptions import ObjectDoesNotExist

from .models import PersonalInfo


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


class Courses(View):
    def get(self, request):
        course_list = ["Bio", "English", "Spanish", "CS361"]
        lab_list = [Lab(course='Bio', meet_time='9:30', ta='John Doe'), Lab(course='Gym', meet_time='11:30', ta='Me')]
        return render(request, "courses.html", {"courses": lab_list})

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

