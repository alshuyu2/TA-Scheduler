from enum import Enum
from django.db import models


class Role(models.TextChoices):
    ADMIN = 1
    INSTRUCTOR = 2
    TA = 3
