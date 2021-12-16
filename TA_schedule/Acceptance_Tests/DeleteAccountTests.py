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

    def test_Succ_Create(self):
        Form_info = {
            'username': 'vinny',
            'email': 'zack@uwm.edu',
            'password1': 'adminadmi%aadn',
            'password2': 'adminadmi%aadn',

        }
        # self.Admin.post("/deleteAccount/", User.objects.get(username= Form_info['username']), follow=True) #go to the deleteAcc and test it

        self.Admin.post("/CreateAcc/", Form_info, follow=True)
        c_objects = list(User.objects.all())
        self.assertEqual(len(c_objects), 2)  # one for the created acc, + 1 for the Super Admin
        self.Admin.post("/deleteAccount/", {'username': '2'}, follow=True) #go to the deleteAcc and test it
        c_objects = User.objects.count()
        self.assertEqual(c_objects, 1)  # minus one for the created acc


    #Another test to check if the right username has been deleted
class TestDeleteForm(TestCase):

    def setup(self):
        self.u_info = {'username': 'Vince', 'password': 'pw123'}
        User.objects.create_user(**self.u_info)
        # self.dictionary = (self.u_info)
        # for i in range(4):
        #     self.u_info['username'] = str(i)
        #     User.objects.create_user(**self.u_info)

    def test_valid_form(self):
        self.dict = {'username': '1'}
        del_form = RemoveUserForm(self.dict)
        self.assertTrue(del_form.is_valid())

    def test_invalid_empty_form(self):
        self.assertFalse(RemoveUserForm().is_valid(), msg='invalid form')



    # def test_invalid_not_a_username(self):
    #
    #     self.assertFalse(RemoveUserForm({'username': '6'}).is_valid()) #check with with context if it doesn't work

    # def test_invalid_one_arg(self):
    #     self.assertFalse(RemoveUserForm({'class_name': '1'}).is_valid())
    #
    # def test_invalid_one_arg_other(self):
    #     self.assertFalse(RemoveUserForm({'ta_name': '1'}).is_valid())