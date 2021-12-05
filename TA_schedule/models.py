from django.contrib.auth.models import User
from django.db import models
from .roles import Role


class PersonalInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=10)
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.ADMIN)
    address = models.CharField(max_length=25, default='')
    office_hours = models.CharField(max_length=50, default='')


class Class(models.Model):
    name = models.CharField(max_length=20)
    instr_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    # def __str__(self):
    #     return User.username


class TAtoClass(models.Model):
    class_name = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)
    ta_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class Lab(models.Model):
    section = models.CharField(max_length=20)
    ta_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class ClassToLab(models.Model):
    class_id = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)
    lab_id = models.ForeignKey(Lab, on_delete=models.SET_NULL, null=True)

