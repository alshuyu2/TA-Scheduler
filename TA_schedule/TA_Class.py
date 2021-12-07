from datetime import datetime
# import str
# import instructor
# import TA
# import labs
# from instructor import Instructor
# import TA_schedule.Lab


class TA:
    def __init__(self, name='', email='', phone='', address='', office_hours='', labs=None, courses=None):
        if labs is None:
            labs = []
        if courses is None:
            courses = []
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.labs = labs
        self.hours = office_hours

    def set_name(self, given_name):
        # if not isinstance(given_name, str):
        #     raise TypeError("Name must be of type str")

        self.name = given_name

    def get_name(self):
        return self.name

    def set_email(self, given_email):
        # if not isinstance(given_email, str):
        #     raise TypeError("Email must be of type str")

        self.email = given_email

    def get_email(self):
        return self.email

    def set_phone(self, given_phone):
        # if not isinstance(given_phone, str):
        #     raise TypeError("Phone must be of type str")

        self.phone = given_phone

    def get_phone(self):
        return self.phone

    def set_address(self, given_address):
        # if not isinstance(self, given_address):
        #     raise TypeError("Address must be of type str")
        self.address = given_address

    def get_address(self):
        return self.address

    def get_labs(self):
        return self.labs

    def set_hours(self, given_hours):
        # if not isinstance(given_hours, datetime):
        #     raise TypeError("Argument is not of type datetime")

        self.hours = given_hours

    def get_hours(self):
        return self.hours

    def get_contact_info(self):
        self.get_email() + "," + self.get_phone() + "," + self.get_hours()

    def add_lab(self, given_lab):
        # if not isinstance(given_lab, Lab.Lab):
        #     raise TypeError("Lab must be of type lab")
        self.labs.append(given_lab)

    # def remove_lab(self, given_lab):
    #     # if not isinstance(given_lab, Lab):
    #     #     raise TypeError("Lab must be of type lab")
    #     self.labs.remove(given_lab)

    # def get_course(self):
    #     return self
