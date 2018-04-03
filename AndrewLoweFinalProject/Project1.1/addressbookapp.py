from mainframe import *
from addressbook import *

__author__ = 'Andrew'


# date modified: 11/21/2016

# The AddressBookApp is responsible for running the program
class AddressBookApp(App):
    # constructor method
    def __init__(self):
        print("CREATING APP")
        self.addressbook = AddressBook()
        # Must be last line because it starts an infinite loop
        self.mainFrame = MainFrame(self)

    # add function is used to override the add function located in mainframe
    def add(self, lname, fname, pnum, email, address):
        self.addressbook.add(lname, fname, pnum, email, address)

    # update function is used to override the update function located in mainframe
    def update(self, contact):
        self.addressbook.update(contact)


# run program
AddressBookApp()
