import django.test
from TA_schedule.models import User
from django.test import Client, TestCase


class Good_CreateAcc(TestCase):
    def setUp(self):
        self.Admin = Client()
        self.info = {
            'username': 'zack',
            'password': '1234',
        }
        self.u = User.objects.create_user(**self.info)  # Creates a user
        self.Admin.login(**self.info)  # used to login to the page

    def test_Succ_Create(self):
        Form_info = {
            'username': 'vinny',
            'email': 'zack@uwm.edu',
            'password': '1234',
            'office_hours': "2 AM",
            'phone': '414',
            'role': '2',
        }
        resp = self.Admin.post("/CreateAcc/", Form_info, follow=True)
        c_objects = list(User.objects.all())
        print(len(c_objects))
        self.assertEqual(len(c_objects), 2)  # one for the created acc, + 1 for the Super Admin

        # print(c_objects)

    def test_Succ_Create_two_users(self):
        Form_info = {
            'username': 'vinny',
            'email': 'zack@uwm.edu',
            'password': '1234',
            'office_hours': "2 AM",
            'phone': '414',
            'role': '1',
        }
        Form_info2 = {
            'username': 'ben',
            'email': 'ben@uwm.edu',
            'password': '123',
            'office_hours': "2 AM",
            'phone': '414',
            'role': '1',
        }
        resp = self.Admin.post("/CreateAcc/", Form_info, follow=True)
        print(resp)
        resp2 = self.Admin.post("/CreateAcc/", Form_info2, follow=True)
        print(resp2)
        c_objects = list(User.objects.all())
        print(len(c_objects))
        self.assertEqual(len(c_objects), 3)  # two for the created acc, + 1 for the Super Admin

    def test_Succ_Create_three_users(self):
        Form_info = {
            'username': 'vinny',
            'email': 'zack@uwm.edu',
            'password': '1234',
            'office_hours': "2 AM",
            'phone': '414',
            'role': '1',
        }
        Form_info2 = {
            'username': 'ben',
            'email': 'ben@uwm.edu',
            'password': '123',
            'office_hours': "2 AM",
            'phone': '414',
            'role': '1',
        }
        Form_info3 = {
            'username': 'Jake',
            'email': 'ben@uwm.edu',
            'password': '123',
            'office_hours': "2 AM",
            'phone': '414',
            'role': '1',
        }
        resp = self.Admin.post("/CreateAcc/", Form_info, follow=True)
        print(resp)
        resp2 = self.Admin.post("/CreateAcc/", Form_info2, follow=True)
        print(resp2)
        resp3 = self.Admin.post("/CreateAcc/", Form_info3, follow=True)
        print(resp2)
        c_objects = list(User.objects.all())
        print(len(c_objects))
        self.assertEqual(len(c_objects), 4)  # 3 for the created acc, + 1 for the Super Admin

    def test_succ_Create_many_users(self):
        names = ["a", "b", "c", "d", "as", "fasfa", "Benny", "alex"]
        for i in names:
             Form_info = {
                    'username': i,
                    'email': 'zack@uwm.edu',
                    'password': '1234',
                    'office_hours': "2 AM",
                    'phone': '414',
                    'role': '1',
             }

             resp = self.Admin.post("/CreateAcc/", Form_info, follow=True)

        c_objects = list(User.objects.all())
        print(len(c_objects))
        self.assertEqual(len(c_objects), 9)  # 8 for the created acc, + 1 for the Super Admin

class Bad_CreateAcc(TestCase):

    def setUp(self):
        self.Admin = Client()
        self.info = {
            'username': 'zack',
            'password': '1234',
        }
        self.u = User.objects.create_user(**self.info)
        self.Admin.login(**self.info)

    def test_create_same_User(self):
        Form_info = {
            'username': 'zack',
            'email': 'zack@uwm.edu',
            'password': '1234',
            'office_hours': "2 AM",
            'phone': '414',
            'role': '1',
        }

        resp = self.Admin.post("/CreateAcc", self.info, follow=True)
        resp2 = self.Admin.post("/CreateAcc/", Form_info, follow=True)
        self.assertEqual(resp2.request["PATH_INFO"], '/CreateAcc/')

    def test_create_User_No_pass(self):
        Form_info = {
            'username': 'ben',
            'email': 'ben@uwm.edu',
            'password': '',
            'office_hours': "2 AM",
            'phone': '414',
            'role': '1',
        }
        resp = self.Admin.post("/CreateAcc/", Form_info, follow=True)
        self.assertEqual(resp.request["PATH_INFO"], '/CreateAcc/')

    def test_create_User_No_Username(self):
        Form_info = {
            'username': '',
            'email': 'ben@uwm.edu',
            'password': '12414',
            'office_hours': "2 AM",
            'phone': '414',
            'role': '1',
        }
        resp = self.Admin.post("/CreateAcc/", Form_info, follow=True)
        self.assertEqual(resp.request["PATH_INFO"], '/CreateAcc/')

    def test_create_User_No_Email(self):
        Form_info = {
            'username': 'Gary',
            'email': '',
            'password': '114',
            'office_hours': "2 AM",
            'phone': '414',
            'role': '1',
        }
        resp = self.Admin.post("/CreateAcc/", Form_info, follow=True)
        self.assertEqual(resp.request["PATH_INFO"], '/CreateAcc/')

    def test_create_Empty_User(self):
        Form_info = {
            'username': '',
            'email': '',
            'password': '',
            'office_hours': '',
            'phone': '',
            'role': '',
        }
        resp = self.Admin.post("/CreateAcc/", Form_info, follow=True)
        self.assertEqual(resp.request["PATH_INFO"], '/CreateAcc/')

#
# class  test_Admin_UnSuc_account(TestCase):
#     def setUp(self):
#         self.Admin = Client()
#         self.info = {
#             'username': 'zack',
#             'email': 'Zemui@uwm.edu',
#             'password': '1234',
#             #'office_hours': '12:00',
#             #'phone': '414',
#         }
#         User.objects.create_user(**self.info)
#         self.Admin.login(**self.info)
#
#     # def test_Admin_Create_Same_account(self):
#     #     resp = self.Admin.post('/CreateAcc', **self.info)
#     #     self.assertNotEqual(resp.context["message"], 'Your account has been Created!', msg="test is working")
#     #     resp2 = self.Admin.post('/CreateAcc', **self.info)
#     #     self.assertEqual(resp2.context["message"], "Your account could not be Created", msg="test is working")
#     #
#     # def test_Admin_no_email(self):
#     #     resp = self.Admin.post('/CreateAcc', {"Username": "Ben", "Email": " ", "Password": "1234"})
#     #     self.assertEqual(resp.context["message"], "Your account could not be Created", msg="test is working")
#
#
