from abc import ABC, abstractmethod


class UserInterface(ABC):

    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def getEmail(self):
        pass

    @abstractmethod
    def getPhone(self):
        pass

    @abstractmethod
    def getContactInfo(self):
        pass

    @abstractmethod
    def getOfficeHour(self):
        pass

    @abstractmethod
    def getAddress(self):
        pass

    @abstractmethod
    def setName(self, other):
        pass

    @abstractmethod
    def getEmail(self):
        pass

    @abstractmethod
    def setPhone(self, other):
        pass

    @abstractmethod
    def setContactInfo(self, other):
        pass

    @abstractmethod
    def setOfficeHour(self, other):
        pass

    @abstractmethod
    def setAddress(self, other):
        pass