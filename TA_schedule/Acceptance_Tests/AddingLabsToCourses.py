from django.test import TestCase, Client
from TA_schedule.models import PersonalInfo, Class, ClassToLab, TAtoClass, Lab, User
from TA_schedule import views
import unittest


# Create your tests here.
# class ClassToLabSetup(TestCase):
#     def setUp(self) -> None:
#         self.user = Client()
#         self.class_lab = Class(name="Math315")
#         self.lab_ofclass = Lab(section="Lab2")
#         self.labToClass = ClassToLab(class_id=self.class_lab, lab_id=self.lab_ofclass)
from TA_schedule.roles import Role


class ClassToLab(TestCase):
    def setUp(self) -> None:
        self.user = Client()
        self.info = {'username': 'Zack', 'password': 'pw123'}
        self.u = User.objects.create_user(**self.info)
        self.user.login(**self.info)
        self.u2 = User.objects.create_user(username="Vince", password="abcdef")
        self.p_info = PersonalInfo.objects.get(user__username=self.info['username'])
        self.p_info.role = Role.INSTRUCTOR
        self.p_info.save()

        self.p_info = PersonalInfo.objects.get(user__username="Vince")
        self.p_info.role = Role.TA
        self.p_info.save()
        # self.class_lab = Class(name="Math315")
        # self.lab_ofclass = Lab(section="Lab2")
        # self.labToClass = ClassToLab(class_id=self.class_lab, lab_id=self.lab_ofclass)
        Class.objects.create(name="Adriana", instr_id=self.u)
        Lab.objects.create(section="901", ta_name=self.u2)

    def test_addLab(self):
        # verify that a user can log in
        # anything = ClassToLab.objects.count()
        response = self.client.post("/addLabs/", {"labName": "Math315", "course": "1"}, follow=True)
        anything2 = ClassToLab.objects.count()
        self.assertEqual(1, anything2)

    # def test_addLab1(self):
    #     # verify that a user can log in
    #     response = self.client.post("/addLabs/", {"name": "Math315", "instr_id": "", "section": "Lab2","ta_name":""}, follow=True)
    #     #response2 = client2.post("/addLabs/", {"name": "Math31", "instr_id": "", "section": "Lab2", "ta_name": ""}, follow=True)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response2.status_code, 200)


    def test_addLab4(self):
        client = Client()
        client2 = Client()
        response = client.post("/addLabs/", {"name": "CS351", "instr_id": "John Doe", "section": "Lab2","ta_name":""}, follow=True)
        response2 = client2.post("/addLabs/", {"name": "English101", "instr_id": "Cathy", "section": "", "ta_name": ""},follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response2.status_code, 200)

    def test_addLab5(self):
        client = Client()
        client2 = Client()
        response = client.post("/addLabs/", {"name": "", "section": "Lab2","ta_name":""}, follow=True)
        response2 = client2.post("/addLabs/", {"name": "English101", "instr_id": "Cathy", "section": "", "ta_name": ""},follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response2.status_code, 200)

    def test_addLab6(self):
        client = Client()
        # verify that a user can log in
        response = client.post("/addLabs/", {"name": "Englist", "instr_id": "", "section": "Lab21", "ta_name": ""},
                               follow=True)
        self.assertEqual(response.status_code, 200)