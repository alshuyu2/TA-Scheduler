from enum import Enum
from django.db import models

#
# def forDjango(cls):
#     cls.do_not_call_in_templates = True
#     return cls
#
# @forDjango
class Role(models.TextChoices):
    ADMIN = 1
    INSTRUCTOR = 2
    TA = 3
