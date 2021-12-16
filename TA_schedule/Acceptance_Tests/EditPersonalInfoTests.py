from django.contrib.auth.models import User
from django.test import TestCase, Client


# username
# email
# office_hours
# phone
from TA_schedule.models import PersonalInfo
from TA_schedule.roles import Role


class EditInfo(TestCase):
    def setUp(self) -> None:
        self.info = {
            'username': 'Vince',
            'password': 'pw123',
            'email': 'test@uwm.edu'
        }
        self.u = User.objects.create_user(**self.info)
        emp = PersonalInfo.objects.get(user=self.u)
        emp.phone = '4149999999'
        emp.office_hours = '11-12 monday-friday'
        emp.address = 'my house'
        emp.save()
        # print(list(PersonalInfo.objects.all().values()))
        self.user = Client()
        self.user.login(**self.info)

    def test_edit_username(self):
        new_info = {
            'username': 'asdf',
            'email': 'test@uwm.edu',
            'password': 'pw123',
            'office_hours': '11-12 monday-friday',
            'phone': '4149999999',
            'address': 'UWM street'
        }
        self.user.post('/profile/', new_info, follow=True)
        db_obj = list(User.objects.all().values()).pop()
        # print(db_obj)
        self.assertEqual(db_obj['username'], new_info['username'])

    def test_edit_username_dup(self):
        # set current user's username to a taken username. redirect back to profile without updating
        new_info = {
            'username': 'Greg',
            'email': 'test@uwm.edu',
            'password': 'pw123',
            'office_hours': '11-12 monday-friday',
            'phone': '4149999999',
            'address': 'UWM street'
        }
        greg = {
            'username': 'Greg',
            'password': 'pw12',
            'email': 'test2@uwm.edu',
        }
        User.objects.create_user(**greg)
        response = self.user.post('/profile/', new_info, follow=True)
        self.assertEqual(response.request['PATH_INFO'], '/profile/')

    # TODO bad email
    def test_edit_email(self):
        new_info = {
            'username': 'Vince',
            'email': 'banana@uwm.edu',
            'password': 'pw123',
            'office_hours': '11-12 monday-friday',
            'phone': '4149999999',
            'address': 'UWM street'
        }
        self.user.post('/profile/', new_info, follow=True)
        db_obj = list(User.objects.all().values()).pop()
        # print(db_obj)
        self.assertEqual(db_obj['email'], new_info['email'])

    def test_edit_email_invalid(self):
        # invalid email redirect back to profile
        new_info = {
            'username': 'Vince',
            'email': 'banana',
            'password': 'pw123',
            'office_hours': '11-12 monday-friday',
            'phone': '4149999999',
            'address': 'UWM street'
        }
        response = self.user.post('/profile/', new_info, follow=True)
        # db_obj = list(User.objects.all().values()).pop()
        # print(db_obj)
        self.assertEqual(response.request['PATH_INFO'], '/profile/')

    def test_edit_office_hours(self):
        new_info = {
            'username': 'Vince',
            'email': 'test@uwm.edu',
            'password': 'pw123',
            'office_hours': '8-9 T/TH',
            'phone': '4149999999',
            'address': 'UWM street'
        }
        self.user.post('/profile/', new_info, follow=True)
        db_obj = list(PersonalInfo.objects.all().values()).pop()
        # print(db_obj)
        self.assertEqual(db_obj['office_hours'], new_info['office_hours'])

    def test_edit_phone(self):
        new_info = {
            'username': 'Vince',
            'email': 'test@uwm.edu',
            'password': 'pw123',
            'office_hours': '11-12 monday-friday',
            'phone': '414111222',
            'address': 'UWM street'
        }

        self.user.post('/profile/', new_info, follow=True)
        db_obj = list(PersonalInfo.objects.all().values()).pop()
        # print(db_obj)
        self.assertEqual(db_obj['phone'], new_info['phone'])

    def test_valid_edit_redirect(self):

        new_info = {
            'username': 'asdf',
            'email': 'asdf@uwm.edu',
            'password': 'asdf',
            'office_hours': 'Never',
            'phone': '9876543210',
            'address': 'UWM street'
        }

        response = self.user.post('/profile/', new_info, follow=True)
        # db_obj = list(User.objects.all().values()).pop()
        # print(db_obj)
        self.assertEqual(response.request['PATH_INFO'], '/dashboard/')

