from django.test import TestCase, Client
from TA_schedule.models import User, PersonalInfo
from TA_schedule.forms import RemoveUserForm
from TA_schedule.roles import Role


class Good_DeleteAcc(TestCase):
    def setUp(self):
        self.Admin = Client()
        self.info = {
            'username': 'zack',
            'password': '1234',
        }
        self.u = User.objects.create_user(**self.info)  # Creates a super user
        self.Admin.login(**self.info)  # used to login to the page
        for i in range(2,6):
            self.info['username'] = str(i)
            User.objects.create_user(**self.info)

    def test_Succ_Create(self):
        # Form_info = {
        #     'username': 'vinny',
        #     'email': 'zack@uwm.edu',
        #     'password1': 'adminadmi%aadn',
        #     'password2': 'adminadmi%aadn',
        #
        # }
        # # self.Admin.post("/deleteAccount/", User.objects.get(username= Form_info['username']), follow=True) #go to the deleteAcc and test it
        #
        # self.Admin.post("/CreateAcc/", Form_info, follow=True)
        c_objects = list(User.objects.all())
        self.assertEqual(len(c_objects), 5)  # one for the created acc, + 1 for the Super Admin
        self.Admin.post("/deleteAccount/", {'username': '2'}, follow=True)  # go to the deleteAcc and test it
        c_objects = User.objects.count()
        self.assertEqual(c_objects, 4)  # minus one for the created acc

    # Another test to check if the right username has been deleted
    # Do a post request and try to search the name for it
    def test_delete(self):
        self.Admin.post("/deleteAccount/", {'username': '1'}, follow=True)
        var = list(User.objects.filter(username= 'zack'))
        self.assertListEqual(var, [], msg="Both lists are empty")

    def test_size(self):
        c_objects = User.objects.count()
        self.Admin.post("/deleteAccount/", {'username': '1'}, follow=True)
        var = User.objects.count()
        self.assertEqual(c_objects - 1, var, msg="it works")
class TestDeleteForm(TestCase):

    def setUp(self) -> None:
        self.u_info = {'username': 'Vince', 'password': 'pw123'}
        User.objects.create_user(**self.u_info)
        for i in range(4):
            self.u_info['username'] = str(i)
            User.objects.create_user(**self.u_info)

    def test_valid_form(self):
        self.dict = {'username': '1'}
        del_form = RemoveUserForm({'username': '1'})
        self.assertTrue(del_form.is_valid())

    def test_invalid_empty_form(self):
        self.assertFalse(RemoveUserForm().is_valid(), msg='invalid form')

    def test_not_username(self):
        with self.assertRaises(KeyError, msg='Username is invalid'):
            RemoveUserForm({'username': '6'}).is_valid()
