from customtkinter import *

import db_connection
from utils.ui_utils import create_entry
from CTkMessagebox import CTkMessagebox
from db_connection import cursor
def clear_entries(root: CTk):

    global auth_win, user_entry, pass_entry

    auth_win = CTkToplevel(root)
    auth_win.geometry('400x300')
    auth_win.focus_set()
    auth_win.grab_set()
    auth_win.resizable(False, False)
    auth_win.title('Clear Entries')

    CTkLabel(auth_win, text="Authorization Window", font=('', 20)).place(relx=0.3, rely=0.1)


    user_lbl = CTkLabel(auth_win, text='username- ')
    user_lbl.place(relx=0.1, rely=0.30)

    user_entry = create_entry(auth_win,  show='*')
    user_entry.place(relx=0.35, rely=0.30)

    pass_lbl = CTkLabel(auth_win, text='password- ')
    pass_lbl.place(relx=0.1, rely=0.45)

    pass_entry = create_entry(auth_win, show='*')
    pass_entry.place(relx=0.35, rely=0.45)

    del_btn = CTkButton(auth_win, text="Delete",
                     command=confirm_clear_entries)

    del_btn.place(relx=0.35, rely=0.6)


def confirm_clear_entries():

    username = user_entry.get()
    password = pass_entry.get()

    msgbox = CTkMessagebox(title="Clear Entries?", message="Are you sure you want to clear all the entries?",
                        icon="question", option_1="Cancel", option_2="No", option_3="Yes")
    response = msgbox.get()

    if response == "Yes" and validate_user(username, password):
        delete_entries()
        CTkMessagebox(title="Info", message="All entries have been deleted.", icon="info")
    else:
        CTkMessagebox(title="Error", message="Invalid credentials! Try again.", icon="cancel")

def validate_user(username: str, password: str):
    cursor.execute('select * from authentication where name=%s and password = %s', (username, password))
    result = cursor.fetchone()

    if result:
        return True

def delete_entries():
    cursor.execute('truncate table customers')
    db_connection.db_conn.commit()
    auth_win.destroy()
