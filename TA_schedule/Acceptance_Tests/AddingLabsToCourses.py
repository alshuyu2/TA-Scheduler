from django.test import TestCase, Client
from TA_schedule.models import PersonalInfo, Class, ClassToLab, TAtoClass, Lab, User
from TA_schedule import views
import unittest


# Create your tests here.
class ClassToLabSetup(TestCase):
    def setUp(self) -> None:
        self.user = Client()
        self.class_lab = Class(name="Math315")
        self.lab_ofclass = Lab(section="Lab2")
        self.labToClass = ClassToLab(class_id=self.class_lab, lab_id=self.lab_ofclass)

class ClassToLab(TestCase):
    def test_addLab(self):
        client = Client()
        # verify that a user can log in
        response = client.post("/addLabs/", {"name": "Math315", "instr_id": "", "section": "Lab2","ta_name":""}, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_addLab1(self):
        client = Client()
        client2 = Client()
        # verify that a user can log in
        response = client.post("/addLabs/", {"name": "Math315", "instr_id": "", "section": "Lab2","ta_name":""}, follow=True)
        response2 = client2.post("/addLabs/", {"name": "Math31", "instr_id": "", "section": "Lab2", "ta_name": ""},
                               follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response2.status_code, 200)


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

