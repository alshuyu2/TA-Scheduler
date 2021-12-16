from django.test import TestCase, Client
from TA_schedule.models import User, PersonalInfo
from TA_schedule.forms import SkillsUpdateForm


class FormValid(TestCase):
    def test_valid_form(self):
        self.assertFalse(SkillsUpdateForm().is_valid(), msg='empty form not valid')

    def test_invalid_form(self):
        ta_form = SkillsUpdateForm(data={'skills': 'not empty'})
        self.assertTrue(ta_form.is_valid())


class SkillsEmpty(TestCase):
    def setUp(self) -> None:
        self.user = Client()
        self.u_info = {
            'username': 'Vince',
            'password': 'pw123'
        }
        User.objects.create_user(**self.u_info)
        self.user.login(**self.u_info)

    def test_skills_default(self):
        self.assertEqual(PersonalInfo.objects.get(user__username=self.u_info['username']).skills, '')

    def test_add_skills(self):
        skills = 'Python, Django, HTML'
        self.user.post('/skills/', {'skills': skills})
        self.assertEqual(PersonalInfo.objects.get(user__username=self.u_info['username']).skills,
                         skills)


class SkillsUpdate(TestCase):
    def setUp(self) -> None:
        self.user = Client()
        self.u_info = {
            'username': 'Vince',
            'password': 'pw123'
        }
        User.objects.create_user(**self.u_info)
        self.user.login(**self.u_info)
        skills = 'Python, Django, HTML'
        self.user.post('/skills/', {'skills': skills})

    def test_update_skills(self):
        new_skills = 'Python, Django, HTML, creating bugs, procrastinating'
        self.user.post('/skills/', {'skills': new_skills})
        self.assertEqual(PersonalInfo.objects.get(user__username=self.u_info['username']).skills,
                         new_skills)
