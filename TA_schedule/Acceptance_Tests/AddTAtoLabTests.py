from django.test import TestCase, Client
from TA_schedule.models import PersonalInfo, Class, ClassToLab, TAtoClass, Lab, User
from TA_schedule import views
from TA_schedule.roles import Role


class ClassToLabTests(TestCase):

    def setUp(self) -> None:
        self.user = Client()
        self.info = {'username': 'Zack', 'password': 'pw123'}
        self.user.login(**self.info)

        #new TA
        self.u = User.objects.create_user(username="Vince", password="abcdef")
        self.p_info = PersonalInfo.objects.get(user__username="Vince")
        self.p_info.role = Role.TA
        self.p_info.save()

        # new TA
        self.u2 = User.objects.create_user(username="Adriana", password="1234")
        self.p_info = PersonalInfo.objects.get(user__username="Adriana")
        self.p_info.role = Role.TA
        self.p_info.save()

        Lab.objects.create(section="901", ta_name=self.u)
        Lab.objects.create(section="102", ta_name=self.u2)

    #There should only be two sections at this point
    def test_totalSectionsPresent(self):
        context = {'TAa': "Vince", 'TAa': "Adriana"}
        self.user.post("/getTA/", context, follow=True)
        lab_objs = Lab.objects.count()
        self.assertEqual(2, lab_objs)

    def test_tAsNotPresent(self):
        context = {'TAa': "Vince", 'TAa': "Adriana"}
        self.user.post("/getTA/", context, follow=True)
        user_objs = User.objects.count()
        self.assertEqual(2, user_objs)

    def test_tAsNotPresent(self):
        context = {'TAa': "Vince", 'TAa': "Adriana"}
        self.user.post("/getTA/", context, follow=True)
        user_objs = User.objects.count()
        self.assertEqual(2, user_objs)

    #There should be one section named 901
    def test_sectionPresent(self):
        context = {'TAa': "Vince", 'TAa' : "Adriana"}
        self.user.post("/getTA/", context, follow=True)
        lab_objs1 = Lab.objects.filter(section=901)
        self.assertEqual(lab_objs1.count(), 1)

    # # There should be one section named 102
    def test_sectionPresent2(self):
        context = {'TAa': "Vince", 'TAa' : "Adriana"}
        self.user.post("/getTA/", context, follow=True)
        lab_objs1 = Lab.objects.filter(section=102)
        self.assertEqual(lab_objs1.count(), 1)

    #Assigning a new TA overrides the old?
    def test_sectionNotPresent(self):
        context = {'TAa': "Vince", 'TAa': "Adriana"}
        self.user.post("/getTA/", context, follow=True)
        lab_objs2 = Lab.objects.filter(section=111)
        self.assertEqual(lab_objs2.count(), 0)




