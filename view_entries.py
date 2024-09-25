from customtkinter import *
import tkinter.ttk as ttk
from db_connection import cursor

def view_entries(root: CTk):
    view_entries_win = CTkToplevel(root)
    view_entries_win.title("View Entries")
    view_entries_win.focus_set()
    view_entries_win.grab_set()

    tree_view = ttk.Treeview(view_entries_win, selectmode=BROWSE)
    tree_view.pack(side=LEFT, fill=BOTH, expand=True)

    # constructing the vertical scrollbar
    verscrlbar = ttk.Scrollbar(view_entries_win, orient=VERTICAL, command=tree_view.yview)
    verscrlbar.pack(side=RIGHT, fill=BOTH)

    tree_view.configure(xscrollcommand=verscrlbar.set)

    tree_view['columns'] = ('id', 'name', 'address', 'paid', 'remaining', 'time', 'date')

    tree_view['show'] = 'headings'

    tree_view.column('id', width=3, anchor=CENTER)
    tree_view.column('name', anchor=CENTER)
    tree_view.column('address', anchor=CENTER)
    tree_view.column('paid', anchor=CENTER)
    tree_view.column('remaining', anchor=CENTER)
    tree_view.column('time', anchor=CENTER)
    tree_view.column('date', anchor=CENTER)

    tree_view.heading('id', text='ID')
    tree_view.heading('name', text='Name')
    tree_view.heading('address', text='Address')
    tree_view.heading('paid', text='Paid')
    tree_view.heading('remaining', text='Remaining')
    tree_view.heading('time', text='Time')
    tree_view.heading('date', text='Date')


    # get the data from db and display it

    cursor.execute('SELECT * FROM customers order by name asc')
    details = cursor.fetchall()

    for data in details:
        tree_view.insert('', 'end', iid=data[0], text=data[0], values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
