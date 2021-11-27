from django.contrib import admin
from .models import MyUser, Classes, ClassEnrollment, Lab, LabEnrollment, PersonalInfo
# Register your models here.
admin.site.register(Classes)
admin.site.register(MyUser)
admin.site.register(ClassEnrollment)
admin.site.register(Lab)
admin.site.register(LabEnrollment)
admin.site.register(PersonalInfo)
