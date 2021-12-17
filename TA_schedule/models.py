from django.contrib.auth.models import User
from django.db import models
from .roles import Role


class PersonalInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=10)
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.ADMIN)
    address = models.CharField(max_length=25, default='')
    office_hours = models.CharField(max_length=50, default='')
    skills = models.CharField(max_length=250, default='')

    # def __str__(self):
    #     return self.user.username


class Class(models.Model):
    name = models.CharField(max_length=20)
    instr_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.name} - {self.instr_id}'


class TAtoClass(models.Model):
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE, null=True)
    ta_name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.ta_name} - {self.class_name} '


class Lab(models.Model):
    section = models.CharField(max_length=20)
    ta_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.section


class ClassToLab(models.Model):
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE, null=True)
    lab_id = models.ForeignKey(Lab, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.class_id} - {self.lab_id}'
