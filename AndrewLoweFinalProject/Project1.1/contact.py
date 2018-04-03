import re

__author__ = 'Andrew'


# date modified: 11/21/2016

# Contact Class
class Contact:
    # constructor for Contact class
    def __init__(self, id, last_name, first_name, phone_number, email, address):
        # Integer
        self._id = id

        # Strings
        self._lastName = last_name
        self._firstName = first_name
        self._phoneNumber = phone_number
        self._email = email
        self._address = address

    def get_id(self):
        """:return contact id"""
        return self._id

    def get_last_name(self):
        """:return contact last name"""
        return self._lastName

    def set_last_name(self, last_name):
        """":param last name"""
        regex = re.compile("^[a-zA-Z-' ]+$")
        if regex.match(last_name) is None:
            raise ValueError("invalid character")
        else:
            self._lastName = last_name

    def get_first_name(self):
        """:return contact first name"""
        return self._firstName

    def set_first_name(self, first_name):
        """:param first_name"""
        regex = re.compile("^[a-zA-Z-' ]+$")
        if regex.match(first_name) is None:
            raise ValueError("invalid character")
        else:
            self._firstName = first_name

    def get_phone_number(self):
        """":return contact phone number"""
        return self._phoneNumber

    def set_phone_number(self, phone_number):
        """:param phone_number"""
        regex = re.compile("^([0-9]{3}-){2}[0-9]{4}$")
        if regex.match(phone_number) is None:
            raise ValueError("invalid character")
        else:
            self._phoneNumber = phone_number

    def get_email(self):
        """return contact email"""
        return self._email

    def set_email(self, email):
        """:param email"""
        regex = re.compile("^[\w!#$%&'*+-/=?^_`{|}~.]+@[\w-]+.[a-z]+$")
        if regex.match(email) is None:
            raise ValueError("invalid character")
        else:
            self._email = email

    def get_address(self):
        """:return contact address"""
        return self._address

    def set_address(self, address):
        """:param address"""
        self._address = address
