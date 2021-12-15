"""TA_schedule URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.contrib.auth import views as auth_views

from TA_schedule.views import Home, DashBoard, Courses, Profile, CourseAdd, CreateAcc, Labs, addLabs,\
    AddTAtoCourse, PublicInfo, SkillPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view()),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('dashboard/', login_required(DashBoard.as_view())),
    path('courses/', login_required(Courses.as_view())),
    path('profile/', login_required(Profile.as_view())),
    path('addcourse/', login_required(CourseAdd.as_view())),
    path('CreateAcc/', login_required(CreateAcc.as_view())),
    path('labs/', login_required(Labs.as_view())),
    path('addLabs/', login_required(addLabs.as_view())),
    path('addtatocourse/', login_required(AddTAtoCourse.as_view())),
    path('publicinformation/', login_required(PublicInfo.as_view())),
    path('skills/', login_required(SkillPage.as_view())),
]
