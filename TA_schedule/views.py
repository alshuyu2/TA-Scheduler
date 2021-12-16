from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render, redirect
from django.views import View

from .UserFactory import UserFactory
from .Lab import Lab
from .forms import UserUpdateForm, PersonalInfoUpdateForm, CourseCreateForm, LabCreateForm, UserCreateForm, \
    PersonalInfoCreateForm, TAtoCourseAddForm, SkillsUpdateForm
# from .forms import UserUpdateForm, PersonalInfoUpdateForm, UserCreateForm

from django.core.exceptions import ObjectDoesNotExist

from .models import PersonalInfo, Class, Lab, ClassToLab, TAtoClass
from .roles import Role



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    try:
        # instance.save()
        instance.personalinfo.save()
    except ObjectDoesNotExist:
        # User.object.create(instance)
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

        # Option 1: both forms are valid and we need to make classtolab object
        # Option 2: c_form is valid and we only create a course. no lab is created, so no CTL needed
        if c_form.is_valid() and l_form.is_valid():
            c_form.save()
            l_form.save()
            # print('about to redirect')
            c = list(Class.objects.filter(name=c_form.cleaned_data.get('name')))
            lab = list(Lab.objects.filter(section=l_form.cleaned_data.get('section')))
            ClassToLab.objects.create(class_id=c.pop(), lab_id=lab.pop())
            messages.success(request, f'Your class and lab has been added!')
            return redirect('/courses/')
        elif c_form.is_valid():
            c_form.save()
            messages.success(request, f'Your class has been added!')
            return redirect('/courses/')
        context = {
            'c_form': c_form,
            'l_form': l_form
        }
        return render(request, "addcourse.html", context)


class Courses(View):
    def __init__(self):
        self.fact = UserFactory()

    def get(self, request):

        # this will have to be done in every method or in init possibly.
        #  all info will be in usr object now
        usr = self.fact.get_user(request.user.personalinfo)

        course_lab_list = []
        for i in usr.get_courses():
            class_lab_list = list(ClassToLab.objects.filter(class_id=i))
            lab_list = []
            ta_to_class = list(TAtoClass.objects.filter(class_name=i, ta_name__personalinfo__role=Role.TA))
            ta_name = []
            for j in class_lab_list:
                lab_list.append(j.lab_id.section)
            for j in ta_to_class:
                ta_name.append(j.ta_name.username)
            course_lab_list.append((i, lab_list, ta_name))
        return render(request, "courses.html", {"courses": course_lab_list})

    def post(self, request):
        return render(request, "courses.html")


class Labs(View):

    def get(self, request):
        allCourses = ClassToLab.objects.all();
        return render(request, "labs.html", {"courses": allCourses})

    def post(self, request):
        return render(request, "labs.html")


class addLabs(View):
    def get(self, request):
        allCourses = ClassToLab.objects.all();
        allTA= PersonalInfo.objects.filter(role=3);
        # # allTA = PersonalInfo.objects.all();
        # allTAs = PersonalInfo.objects.all();
        # allTAa = TAtoClass.objects.all();
        return render(request, "addLabs.html", {"courses": allCourses, "TAs" : allTA})

    def post(self, request):
        class_add = Class.objects.get(name=request.POST["course"])
        new_Lab = Lab(section=request.POST["labName"], ta_name= request.POST["TAa"])
        new_Lab.save()
        new_ClasstoLab = ClassToLab(lab_id=new_Lab, class_id=class_add)
        new_ClasstoLab.save()
        allCourses = ClassToLab.objects.all();
        return render(request, "labs.html", {"courses": allCourses})


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


class CreateAcc(View):
    def get(self, request):
        u_form = UserCreateForm()
        p_form = PersonalInfoCreateForm()
        context = {
            'u_form': u_form,
            'p_form': p_form
        }
        return render(request, "CreateAcc.html", context)

    def post(self, request):
        u_form = UserCreateForm(request.POST)
        # create_user_profile(request.POST)
        # instead of update, create new
        p_form = PersonalInfoCreateForm(request.POST)
        # instead of update, create new

        # print("before validation")
        if u_form.is_valid(): # and p_form.is_valid()
            u_form.save()
            name = User.objects.get(username=request.POST['username'])
            print(name)
            p_form = PersonalInfoCreateForm(request.POST, instance=PersonalInfo.objects.filter(user=name).first())
            if p_form.is_valid():
                # print('valid p_form')
                p_form.save()
            # else:
            #     print('invalid p_form')
            # print("im about to redirect")
            messages.success(request, f'Your account has been Created!')
            return redirect('/dashboard/')
        context = {
            'u_form': u_form,
            # 'p_form': p_form
        }
        messages.error(request, f'Your account could not be Created')
        return render(request, "CreateAcc.html", context)


class AddTAtoCourse(View):

    def get(self, request):
        ta_form = TAtoCourseAddForm()
        context = {
            'ta_form': ta_form,
            'users': PersonalInfo.objects.filter(role=Role.TA)
        }
        return render(request, "addtatocourse.html", context)

    def post(self, request):
        ta_form = TAtoCourseAddForm(request.POST)

        if ta_form.is_valid():
            ta_form.save()
            messages.success(request, f'The ta has been added to the course')
            return redirect('/courses/')
        context = {
            'ta_form': ta_form,
            'users': PersonalInfo.objects.filter(role=Role.TA)
        }
        messages.error(request, f'The ta was not able to be added to the course')
        return render(request, "addtatocourse.html", context)


class PublicInfo(View):
    def get(self, request):
        usr_list = list(PersonalInfo.objects.all())
        users = []
        rev_r = {
            '1': 'Admin',
            '2': 'Instructor',
            '3': 'TA'
        }
        # only way I can figure out how to make role not be a str
        for i in usr_list:
            # print(i.role)
            users.append((i.user.username, rev_r[i.role], i.phone, i.address, i.office_hours, i.skills))

        return render(request, "publicinformation.html", {'usr_list': users})

    def post(self, request):
        return render(request, "publicinformation.html")


class SkillPage(View):
    def get(self, request):
        s_form = SkillsUpdateForm(instance=request.user.personalinfo)
        context = {
            's_form': s_form
        }

        return render(request, "skills.html", context)

    def post(self, request):
        s_form = SkillsUpdateForm(request.POST, instance=request.user.personalinfo)

        if s_form.is_valid():
            s_form.save()
            messages.success(request, f'Skills updated')
            return redirect('/dashboard/')
        context = {
            's_form': s_form
        }
        messages.success(request, f'Skills update failed')
        return render(request, "skills.html", context)
