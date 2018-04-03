from unittest import TestCase
from addressbook import *
from mainframe import *
__author__ = 'Andrew'


# date modified: 11/21/2016

# Use this class to test run the GUI
class TestAddressBookApp(TestCase):
    def __init__(self):
        print("CREATING APP")
        self.addressbook = AddressBook()
        assert isinstance(self.addressbook, AddressBook)
        # Must be last line because it starts an infinite loop
        self.mainFrame = MainFrame(self)

    def test_add(self, lname, fname, pnum, email, address):
        self.addressbook.add(lname, fname, pnum, email, address)

    def test_update(self, contact):
        self.addressbook.update(contact)

TestAddressBookApp()
