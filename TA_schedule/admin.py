from django.contrib import admin
from .models import PersonalInfo, Class, TAtoClass, Lab, ClassToLab
# Register your models here.
admin.site.register(Class)
admin.site.register(ClassToLab)
admin.site.register(Lab)
admin.site.register(TAtoClass)
admin.site.register(PersonalInfo)
