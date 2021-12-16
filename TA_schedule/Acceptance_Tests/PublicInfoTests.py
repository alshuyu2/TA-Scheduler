from django.test import TestCase, Client
from TA_schedule.models import User, PersonalInfo
from TA_schedule.roles import Role


class PublicInfoTests(TestCase):
    def setUp(self) -> None:
        self.user = Client()
        self.u_info = {
            'username': 'Vince',
            'password': 'pw123'
        }
        self.address = 'my house'
        self.phone = '123456'
        self.role = 'TA'
        self.office_hours = '11-12'
        self.skills = 'eating chicken nuggets fast'
        User.objects.create_user(**self.u_info)
        self.user.login(**self.u_info)
        p = PersonalInfo.objects.get(user__username=self.u_info['username'])
        p.role = Role.TA
        p.address = self.address
        p.phone = self.phone
        p.office_hours = self.office_hours
        p.skills = self.skills
        p.save()

    def test_valid_http(self):
        r = self.user.get('/publicinformation/', follow=True)
        self.assertEqual(r.status_code, 200)

    def test_context_size_one(self):
        r = self.user.get('/publicinformation/', follow=True)
        print(r.context['usr_list'])
        self.assertEqual(1, len(r.context['usr_list']))

    def test_context_size_five(self):
        for i in range(4):
            self.u_info['username'] = str(i)
            User.objects.create_user(**self.u_info)

        r = self.user.get('/publicinformation/', follow=True)
        self.assertEqual(5, len(r.context['usr_list']))

    def test_context_username(self):
        r = self.user.get('/publicinformation/', follow=True)
        self.assertEqual(self.u_info['username'], r.context['usr_list'].pop()[0])

    def test_context_role(self):
        r = self.user.get('/publicinformation/', follow=True)
        self.assertEqual(self.role, r.context['usr_list'].pop()[1])

    def test_context_phone(self):
        r = self.user.get('/publicinformation/', follow=True)
        self.assertEqual(self.phone, r.context['usr_list'].pop()[2])

    def test_context_address(self):
        r = self.user.get('/publicinformation/', follow=True)
        self.assertEqual(self.address, r.context['usr_list'].pop()[3])

    def test_context_office_hours(self):
        r = self.user.get('/publicinformation/', follow=True)
        self.assertEqual(self.office_hours, r.context['usr_list'].pop()[4])

    def test_context_skills(self):
        r = self.user.get('/publicinformation/', follow=True)
        self.assertEqual(self.skills, r.context['usr_list'].pop()[5])
