import time
from tkinter import *
from tkinter import messagebox as tkMessageBox
from abc import ABCMeta, abstractmethod

__author__ = 'Andrew'


# date modified: 11/21/2016

# abstract class App
class App:
    # metaclass for defining Abstract Base Class
    __metaclass__ = ABCMeta

    # return type is declared using : str
    # this is not necessary but it can be used to specify the return type
    @abstractmethod
    def add(self, lname: str, fname: str, pnum: str, email: str, address: str): pass


# abstract class submitable
class Submitable:
    # metaclass for defining Abstract Base Class
    __metaclass__ = ABCMeta

    @abstractmethod
    def submit(self): pass


# Mainframe class will be responsible for displaying the selected panel on one frame.
class MainFrame:
    def __init__(self, app):
        # assign window to the Tk class to create the root window
        self.window = Tk()
        # instantiate objects
        self.app = app
        self.mainMenu = MainMenu(self.window, self)

        self.listPanel = ListPanel(self.window, self)

        self.addPanel = AddPanel(self.window, self)
        self.editPanel = EditPanel(self.window, self)

        self.mainMenu.pack()
        self.listPanel.pack()

        self.window.mainloop()

        # Open a file
        file = open("test.txt", "w+")
        # write text
        file.write("Program is running\n")
        # display current time
        file.write(time.strftime("%H:%M:%S"))


# start panel will show the main menu located at the top of the GUI
class MainMenu(Frame):
    # constructor method
    def __init__(self, master, main_frame):
        Frame.__init__(self, master)
        self.mainFrame = main_frame
        self.btnView = Button(self, text="View List", command=self.switch_to_list_panel, width=20).pack(side=LEFT)
        self.btnAdd = Button(self, text="Add Contact", command=self.switch_to_add_panel, width=20).pack(side=LEFT)
        self.btnExit = Button(self, text="Exit", command=self.exit, width=20).pack(side=LEFT)

    # switch to the list view panel when the View List button is selected
    def switch_to_list_panel(self):
        print("Switching to ListView!")
        self.mainFrame.addPanel.pack_forget()
        self.mainFrame.editPanel.pack_forget()
        self.mainFrame.listPanel.pack()
        self.mainFrame.listPanel.populatelistbox()

    # switch to the add panel when the Add button is selected
    def switch_to_add_panel(self):
        print("Switching!")
        self.mainFrame.listPanel.pack_forget()
        self.mainFrame.editPanel.pack_forget()
        self.mainFrame.addPanel.pack()

    def exit(self):
        print("Exiting!")
        print("Goodbye")
        exit()


# list panel will show the view list gui
class ListPanel(Frame):
    # constructor method
    def __init__(self, master, mainframe):
        Frame.__init__(self, master)
        self.mainframe = mainframe
        self.contactList = []
        self.selectedIndex = 0
        self.listbox = Listbox(self, width=74, height=20)
        self.listbox.grid(row=0, column=0, columnspan=2, stick='nsew')
        self.populatelistbox()

        Button(self, text="Edit", command=self.edit).grid(row=2, column=0, columnspan=2, stick='nsew')
        Button(self, text="Delete", command=self.delete).grid(row=3, column=0, columnspan=2, stick='nsew')

    # populate listbox function for list box
    def populatelistbox(self):
        self.listbox.delete(0, END)
        # populate contact list in the list box
        self.contactList = self.mainframe.app.addressbook.get_all_contacts()
        for contact in self.contactList:
            self.listbox.insert(END, contact.get_first_name() + ' ' + contact.get_last_name() + ' ' +
                                '(' + contact.get_phone_number() + ')')

    # delete the contact that is selected in the listbox
    def delete(self):
        try:
            self.selectedIndex = self.listbox.curselection()[0]

            contact = self.contactList.pop(self.selectedIndex)

            self.listbox.delete(self.selectedIndex)

            self.mainframe.app.addressbook.delete(contact)
        except IndexError as ie:
            print("An error occurred:", ie.args[0])

    # edit contact value
    def edit(self):
        try:
            self.selectedIndex = self.listbox.curselection()[0]
            contact = self.contactList[self.selectedIndex]
            self.mainframe.editPanel.load_contact(contact)
            self.mainframe.listPanel.pack_forget()
            self.mainframe.editPanel.pack()
        except IndexError as ie:
            print("An error occurred:", ie.args[0])

    # update the listbox
    def update_list_contact(self, contact):
        self.listbox.delete(self.selectedIndex)

        self.listbox.insert(self.selectedIndex, contact.get_first_name() + contact.get_last_name() +
                            '(' + contact.get_phone_number() + ')')


# Add Panel GUI inherits Submitable
class AddPanel(Submitable):
    """:param Submitable"""

    # constructor method
    def __init__(self, master, mainframe):
        self.mainframe = mainframe
        self.fields = ContactFieldPanel(master, self, "Add")

    # override the submit method in Submitable
    def submit(self):
        # TODO: validate first
        try:
            self.mainframe.app.add(self.fields.lname.get(), self.fields.fname.get(), self.fields.pnum.get(),
                                   self.fields.email.get(), self.fields.address.get())

            self.fields.clear_fields()
        except ValueError as ve:
            tkMessageBox.showinfo(title="Error", message=ve)

    # use the pack method to show the appropriate frames
    def pack(self):
        self.fields.pack()

    # use the pack_forget method to remove the appropriate frames
    def pack_forget(self):
        self.fields.pack_forget()


# Edit Panel GUI inherits Submitable
class EditPanel(Submitable):
    """param Submitable"""

    # constructor method
    def __init__(self, master, mainframe):
        self.master = master
        self.mainframe = mainframe
        self.fields = ContactFieldPanel(master, self, "Update")
        self.contact = None

    # load selected values and assign them to the entries
    def load_contact(self, contact):
        self.contact = contact

        self.fields.clear_fields()
        self.fields.lname.insert(0, contact.get_last_name())
        self.fields.fname.insert(0, contact.get_first_name())
        self.fields.pnum.insert(0, contact.get_phone_number())
        self.fields.email.insert(0, contact.get_email())
        self.fields.address.insert(0, contact.get_address())

    # submit newly entered values
    # override the submit method in Submitable
    def submit(self):
        # TODO: validate first
        try:
            self.contact.set_last_name(self.fields.lname.get())
            self.contact.set_first_name(self.fields.fname.get())
            self.contact.set_phone_number(self.fields.pnum.get())
            self.contact.set_email(self.fields.email.get())
            self.contact.set_address(self.fields.address.get())

            self.mainframe.app.update(self.contact)
            self.mainframe.listPanel.update_list_contact(self.contact)

            self.mainframe.editPanel.pack_forget()
            self.mainframe.listPanel.pack()
        except ValueError as ve:
            tkMessageBox.showinfo(title="Error", message=ve)

    # use the pack method to show the appropriate frames
    def pack(self):
        self.fields.pack()

    # use the pack_forget method to remove the appropriate frames
    def pack_forget(self):
        self.fields.pack_forget()


# edit panel will display the Edit and Add GUIs
class ContactFieldPanel(Frame):
    # constructor method
    def __init__(self, master, submitable, submit_button_text):
        Frame.__init__(self, master)
        Label(self, text="Last Name", width=15).grid(row=0, column=0)
        self.lname = Entry(self, width=55)
        self.lname.grid(row=0, column=1)
        Label(self, text="First Name").grid(row=1, column=0)
        self.fname = Entry(self, width=55)
        self.fname.grid(row=1, column=1)
        Label(self, text="Phone Number").grid(row=2, column=0)
        self.pnum = Entry(self, width=55)
        self.pnum.grid(row=2, column=1)
        Label(self, text="Email").grid(row=3, column=0)
        self.email = Entry(self, width=55)
        self.email.grid(row=3, column=1)
        Label(self, text="Address").grid(row=4, column=0)
        self.address = Entry(self, width=55)
        self.address.grid(row=4, column=1)
        Button(self, text=submit_button_text, command=submitable.submit).grid(row=5, column=0, columnspan=2,
                                                                              stick='nsew')

    # clear fields when switching screens
    def clear_fields(self):
        self.lname.delete(0, END)
        self.fname.delete(0, END)
        self.pnum.delete(0, END)
        self.email.delete(0, END)
        self.address.delete(0, END)
