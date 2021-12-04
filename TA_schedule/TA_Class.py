import string
from datetime import datetime
import instructor
import TA
import labs


class TA(object):
    def __init__(self, name='', email='', phone='', address='',  hours=None, courses=[], labs=[]):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.labs = labs
        self.hours = hours

    def set_name(self, given_name):
        if not isinstance(given_name, string):
            raise TypeError("Name must be of type string")

        self.name = given_name

    def get_name(self):
        return self.name

    def set_email(self, given_email):
        if not isinstance(given_email, string):
            raise TypeError("Email must be of type string")

        self.email = given_email

    def get_email(self):
        return self.email

    def set_phone(self, given_phone):
        if not isinstance(given_phone, string):
            raise TypeError("Phone must be of type string")

        self.phone = given_phone

    def get_phone(self):
        return self.phone

    def set_address(self, given_address):
        if not isinstance(given_address, string):
            raise TypeError("Address must be of type string")
        self.address = given_address

    def get_address(self):
        return self.address

    def get_labs(self):
        return self.labs

    def set_hours(self, given_hours):
        if not isinstance(given_hours, datetime):
            raise TypeError("Argument is not of type datetime")

        self.hours = given_hours

    def get_hours(self):
        return self.hours

    def get_contact_info(self):
        return "Email:" + self.get_email() + "\nPhone Number:" + self.get_phone() + "\nOffice Hours:" + self.get_hours()

    def add_lab(self, given_lab):
        if not isinstance(given_lab, labs):
            raise TypeError("Lab must be of type lab")
        self.labs.append(given_lab)

    def remove_lab(self, given_lab):
        if not isinstance(given_lab, labs):
            raise TypeError("Lab must be of type lab")
        self.labs.remove(given_lab)

