from django.test import TestCase, Client
from TA_schedule.models import PersonalInfo, Class, ClassToLab, TAtoClass, Lab, User
from TA_schedule import views
from TA_schedule.roles import Role


class ClassToLabTests(TestCase):
    def setUp(self) -> None:

        self.user = Client()
        self.info = {'username': 'Zack', 'password': 'pw123'}
        
        self.u = User.objects.create_user(**self.info)
        self.p_info = PersonalInfo.objects.get(user__username=self.info['username'])
        self.p_info.role = Role.INSTRUCTOR
        self.p_info.save()

        self.u2 = User.objects.create_user(username="Vince", password="abcdef")
        self.p_info = PersonalInfo.objects.get(user__username="Vince")
        self.p_info.role = Role.TA
        self.p_info.save()

        self.user.login(**self.info)

        Class.objects.create(name="Adriana", instr_id=self.u)
        Lab.objects.create(section="901", ta_name=self.u2)

    def test_addLab(self):
        context = {'course': 'Adriana', 'labName': 'Lab11'}
        self.user.post("/addLabs/", context, follow=True)
        class_objs = ClassToLab.objects.count()
        self.assertEqual(1, class_objs)

    def test_usersPresent(self):
        context = {'course': 'Adriana', 'labName': 'Lab11'}
        self.user.post("/addLabs/", context, follow=True)
        user_objs = User.objects.count()
        self.assertEqual(2, user_objs)

    def test_classToLabPresent(self):
        context = {'course': 'Adriana', 'labName': '401'}
        self.user.post("/addLabs/", context, follow=True)
        class_objs1 = ClassToLab.objects.filter(class_id__name="Adriana")
        self.assertEqual(class_objs1.count(), 1)

    def test_LabPresent(self):
        context = {'course': 'Adriana', 'labName': '401'}
        self.user.post("/addLabs/", context, follow=True)
        lab_objs1 = Lab.objects.filter(section="401")
        self.assertEqual(lab_objs1.count(), 1)

    def test_LabNotPresent(self):
        context = {'course': 'Adriana', 'labName': '401'}
        self.user.post("/addLabs/", context, follow=True)
        lab_objs1 = Lab.objects.filter(section="111")
        self.assertEqual(lab_objs1.count(), 0)

