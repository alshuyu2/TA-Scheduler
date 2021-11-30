from django.contrib.auth.models import User
from TA_schedule.models import Class, Lab, TAtoClass, ClassToLab, PersonalInfo
from TA_schedule.roles import Role


# TODO import properly

class Instructor:
    pass


class TA:
    pass


class Admin:
    pass


# take in database call to user.
# return an object of correct role
class UserFactory:
    # User(first_name='John', last_name='Doe', email='wildmudkip@gmail.com').save()
    def __init__(self):
        self._creator = None

    def get_user(self, p_info: PersonalInfo):

        name = str(p_info.user_id.first_name + ' ' + p_info.user_id.last_name)
        email = str(p_info.user_id.email)
        phone = int(p_info.phone)
        addr = str(p_info.address)
        office_hour = str(p_info.office_hours)

        if p_info.role == Role.INSTRUCTOR:
            course_list = list(Class.objects.filter(instr_id=p_info.user_id).values_list())
            return Instructor(name=name, email=email, phone=phone, addr=addr, courses=course_list,
                              office_hours=office_hour)
        elif p_info.role == Role.ADMIN:
            return Admin(name=name, email=email, phone=phone, addr=addr)
        elif p_info.role == Role.TA:
            lab_list = list(Lab.objects.filter(ta_name=p_info.user_id).values_list())
            return TA(name=name, email=email, phone=phone, addr=addr, labs=lab_list, office_hours=office_hour)
