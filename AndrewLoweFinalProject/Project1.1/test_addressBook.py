from unittest import TestCase
import sqlite3
from contact import Contact
__author__ = 'Andrew'


# date modified: 11/21/2016

class TestAddressBook(TestCase):
    # test select statement
    def test_get_all_contacts(self):
        contactList = []
        self.__connectionString = "addressBook.db"
        try:
            db_connection = sqlite3.connect(self.__connectionString)
            cursor = db_connection.cursor()

            # Prepare SQL query
            sql = "SELECT * FROM Contact"

            cursor.execute(sql)
            print("Execute SQL")

            resultRows = cursor.fetchall()
            print("Results fetched: ", resultRows)  # [(1, "John", 30),(2, "Mark", 23),(3, "Dohn", 77)]

            for row in resultRows:
                contact = Contact(row[0], row[1], row[2], row[3], row[4], row[5])
                contactList.append(contact)

        except:
            print("Error: unable to fetch data")
        finally:
            db_connection.close()
        assert contactList is not None
        return contactList

    # test Insert statement
    def test_add(self):
        print("adding")
        self.dbConnection = sqlite3.connect("addressBook.db")
        try:
            self.dbConnection.execute(
                "INSERT INTO Contact (last_name,first_name,phone_number,email,address) VALUES ('Lowe', 'Andrew', "
                "'555-5555', 'alowe@mail.com', '123 place street')")

            self.dbConnection.commit()
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
            print("Unable to add")
        finally:
            self.dbConnection.close()

    # test update statement
    def test_update(self):
        self.dbConnection = sqlite3.connect("addressBook.db")
        try:
            self.dbConnection.execute(
                "UPDATE Contact set address = '1240 Collins Ave' where address ='123 place street'")

            self.dbConnection.commit()
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
            print("Unable to add")
        finally:
            self.dbConnection.close()

    # test delete statement
    def test_delete(self):
        self.dbConnection = sqlite3.connect("addressBook.db")
        try:
            self.dbConnection.execute(
                "DELETE from Contact where address='1240 Collins Ave'")

            self.dbConnection.commit()
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
            print("Unable to add")
        finally:
            self.dbConnection.close()