from CTkMessagebox import CTkMessagebox
from customtkinter import *

from db_connection import db_conn, cursor
from utils.ui_utils import create_label, create_entry
from time import strftime
from datetime import datetime


def show_entry_win(root: CTk):
    global name_entry, address_entry, paid_amt_entry, remaining_amt_entry
    add_entry_win = CTkToplevel(root)
    add_entry_win.focus_set()
    add_entry_win.grab_set()
    add_entry_win.geometry("600x500")

    # Title label
    title_lbl = create_label(add_entry_win, text="Add Entry", font_size=30)
    title_lbl.place(relx=0.42, rely=0.1)

    # Name Label and Entry
    name_label = create_label(add_entry_win, text="Name-", font_size=23)
    name_label.place(relx=0.22, rely=0.35)

    name_entry = create_entry(add_entry_win, width=200, height=40)
    name_entry.place(relheight=0.05, relx=0.35, rely=0.35)

    # Address Label and Entry
    address_lbl = create_label(add_entry_win, text="Address-", font_size=23)
    address_lbl.place(relx=0.18, rely=0.45)

    address_entry = create_entry(add_entry_win, width=200, height=40)
    address_entry.place(relheight=0.05, relx=0.35, rely=0.45)

    # Paid Amount Label and Entry
    paid_amt_lbl = create_label(add_entry_win, text="Paid-", font_size=23)
    paid_amt_lbl.place(relx=0.24, rely=0.55)

    paid_amt_entry = create_entry(add_entry_win, width=200, height=40)
    paid_amt_entry.place(relheight=0.05, relx=0.35, rely=0.55)

    # Remaining Amount Label and Entry
    remaining_amt_lbl = create_label(add_entry_win, text="Remaining-", font_size=23)
    remaining_amt_lbl.place(relx=0.14, rely=0.65)

    remaining_amt_entry = create_entry(add_entry_win, width=200, height=40)
    remaining_amt_entry.place(relheight=0.05, relx=0.35, rely=0.65)

    # Submit Button (add this to submit the form)
    submit_btn = CTkButton(add_entry_win, text="Submit", command=submit_entry, height=40)
    submit_btn.place(relx=0.38, rely=0.8)


def validate_inputs(name, address, paid):
    if len(name) == 0:

        CTkMessagebox(title="Error", message="Name cannot be empty!", icon="cancel")
        print(f"Error: Name cannot be empty")
        return False
    elif len(address) == 0:
        print(f"Error: Address cannot be empty")
        CTkMessagebox(title="Error", message="Address cannot be empty!", icon="cancel")
        return False

    elif len(paid) == 0:
        print(f"Error: Paid cannot be empty")
        CTkMessagebox(title="Error", message="Please enter a valid amount!", icon="cancel")
        return False
    return True


def submit_entry():
    name = name_entry.get()
    address = address_entry.get()
    paid_amt = paid_amt_entry.get()
    remaining_amt = remaining_amt_entry.get()



    time = strftime("%I:%D:%S %p")
    current_year = datetime.now().year
    date = strftime(f"%d-%m-{current_year}")

    name = name.title()
    address = address.title()
    paid = paid_amt.title()
    if not validate_inputs(name, address, paid):
        return

    sql_insert_query = '''
        INSERT IGNORE INTO customers (name, address, paid, remaining, time, date)
        values (%s, %s, %s, %s, %s, %s)
    '''

    sql_insert_vals = (name,address, paid_amt, remaining_amt, time, date)

    # execute the sql query
    cursor.execute(sql_insert_query, sql_insert_vals)

    try:
        db_conn.commit()
        # clear the entries
        name_entry.delete(0, END)
        address_entry.delete(0, END)
        paid_amt_entry.delete(0, END)
        remaining_amt_entry.delete(0, END)

        # show info messagebox
        CTkMessagebox(title="Info", message="Records inserted successfully")

    except Exception as e:
        CTkMessagebox(title="Error", message=str(e))


    # print("Entry submitted!")
