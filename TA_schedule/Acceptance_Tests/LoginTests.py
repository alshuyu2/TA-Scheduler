from django.test import TestCase, Client
from TA_schedule.models import User


class LoginValid(TestCase):

    def setUp(self) -> None:
        self.user = Client()
        self.info = {
            'username': 'Vince',
            'password': 'pw123'
        }
        User.objects.create_user(**self.info)

    def test_valid_login(self):
        response = self.user.post('/login/', self.info, follow=True)
        self.assertEqual(response.request['PATH_INFO'], '/dashboard/')

    def test_invalid_login(self):
        response = self.user.post('/login/', {'username': 'John', 'password': 'asdf'}, follow=True)
        self.assertEqual(response.request['PATH_INFO'], '/login/')

    def test_invalid_login_username_wrong(self):
        response = self.user.post('/login/', {'username': 'John', 'password': 'pw123'}, follow=True)
        self.assertEqual(response.request['PATH_INFO'], '/login/')

    def test_invalid_login_password_wrong(self):
        response = self.user.post('/login/', {'username': 'Vince', 'password': 'asdf'}, follow=True)
        self.assertEqual(response.request['PATH_INFO'], '/login/')

    def test_login_redirect(self):
        response = self.user.post('/login/', self.info, follow=True)
        # print(response.request)
        self.assertEqual(response.request['PATH_INFO'], '/dashboard/')


class LogInFirst(TestCase):

    def setUp(self) -> None:
        self.user = Client()
        self.info = {
            'username': 'Vince',
            'password': 'pw123'
        }
        # TODO will keep adding to this as we add more pages
        self.pages = ['/dashboard/', '/courses/', '/profile/', '/addcourse/', '/CreateAcc/', '/addLabs/',
                      '/addtatocourse/', '/labs/', '/publicinformation/', '/skills/']

        User.objects.create_user(**self.info)

    def test_login_required(self):
        for i in self.pages:
            response = self.user.get(i, follow=True)
            self.assertEqual(response.request['PATH_INFO'], '/login/')
