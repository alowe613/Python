from unittest import TestCase
from contact import Contact

__author__ = 'Andrew'


# date modified: 11/21/2016

class TestContact(TestCase):
    def test_get_contact(self):
        # initialize values
        init_id = 5
        init_last_name = 'person'
        init_first_name = 'name'
        init_phone = '123-456-7890'
        init_email = 'email@domain.com'
        init_address = '123 fake street'
        # create object
        contact = Contact(init_id, init_last_name, init_first_name, init_phone, init_email, init_address)

        # run test to check that the assigning of these values work
        self.assertTrue(init_id == contact.get_id(), "ID not set or accessed properly")
        self.assertTrue(init_last_name == contact.get_last_name(), "Last name not set or accessed properly")
        self.assertTrue(init_first_name == contact.get_first_name(), "First name not set or accessed properly")
        self.assertTrue(init_phone == contact.get_phone_number(), "Phone number not set or accessed properly")
        self.assertTrue(init_email == contact.get_email(), "Email not set or accessed properly")
        self.assertTrue(init_address == contact.get_address(), "Address not set or accessed properly")

        # print True to show that the values are being accepted
        print(init_id == contact.get_id())
        print(init_last_name == contact.get_last_name())
        print(init_first_name == contact.get_first_name())
        print(init_phone == contact.get_phone_number())
        print(init_email == contact.get_email())
        print(init_address == contact.get_address())
