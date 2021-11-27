from django.db import models
from .roles import Role


class MyUser(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=20, choices=Role.choices)


class Lab(models.Model):
    name = models.CharField(max_length=20)


class LabEnrollment(models.Model):
    user_id = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)
    lab_id = models.ForeignKey(Lab, on_delete=models.CASCADE, null=True)


class Classes(models.Model):
    name = models.CharField(max_length=20)
    lab_id = models.ForeignKey(Lab, on_delete=models.CASCADE, null=True)


class ClassEnrollment(models.Model):
    user_id = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)
    class_id = models.ForeignKey(Classes, on_delete=models.CASCADE, null=True)


class PersonalInfo(models.Model):
    user_id = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
