import sqlite3
from contact import Contact

__author__ = 'Andrew'


# date modified: 11/21/2016

class AddressBook:
    # constructor method
    def __init__(self):
        self.__connectionString = "addressBook.db"

    def get_all_contacts(self):
        """
        gets all contacts from the database
        :return: List of Contact objects
        """
        contact_list = []

        try:
            db_connection = sqlite3.connect(self.__connectionString)
            cursor = db_connection.cursor()

            # Prepare SQL query
            sql = "SELECT * FROM Contact"

            # execute prepared query
            cursor.execute(sql)
            print("Execute SQL")

            # print results
            result_rows = cursor.fetchall()
            print("Results fetched: ", result_rows)

            for row in result_rows:
                contact = Contact(row[0], row[1], row[2], row[3], row[4], row[5])
                contact_list.append(contact)

        except:
            print("Error: unable to fetch data")
        finally:
            db_connection.close()

        return contact_list

    def add(self, lname, fname, pnum, email, address):
        """:param lname, fname, pnum, email, address
        insert values into database
        """
        print("adding")
        try:
            db_connection = sqlite3.connect(self.__connectionString)
            sql = "INSERT INTO Contact (last_name,first_name,phone_number,email,address) VALUES (" + \
                  "'" + lname + "', " + \
                  "'" + fname + "', " + \
                  "'" + pnum + "', " + \
                  "'" + email + "', " + \
                  "'" + address + "')"

            db_connection.execute(sql)
            db_connection.commit()
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
            print("Unable to add")
        finally:
            db_connection.close()

    def update(self, contact):
        """:param contact
        update contact values
        """
        print("update")
        try:
            db_connection = sqlite3.connect(self.__connectionString)
            sql = "UPDATE Contact set" + \
                  " last_name='" + contact.get_last_name() + "'," + \
                  " first_name='" + contact.get_first_name() + "'," + \
                  " phone_number='" + contact.get_phone_number() + "'," + \
                  " email='" + contact.get_email() + "'," + \
                  " address='" + contact.get_address() + "'" + \
                  " where ID=" + str(contact.get_id())
            print(sql)
            db_connection.execute(sql)
            db_connection.commit()
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
            print("Unable to update")
        finally:
            db_connection.close()

    def delete(self, contact):
        """:param contact
        delete contact from database
        """
        print("delete")
        try:
            db_connection = sqlite3.connect(self.__connectionString)
            sql = "DELETE from Contact where ID=" + str(contact.get_id())

            db_connection.execute(sql)
            db_connection.commit()
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
            print("Unable to delete")
        finally:
            db_connection.close()
