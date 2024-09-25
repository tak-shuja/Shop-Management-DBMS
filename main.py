from db_connection import db_conn
import customtkinter
from utils.ui_utils import *
from add_entry_window import show_entry_win
from view_entries import view_entries
from clear_entries import  clear_entries




if __name__ == '__main__':
    # set appearance and color theme
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")

    # create the root window object
    root = customtkinter.CTk()
    root.title("Shop Management DBMS")
    root.geometry("600x500")
    root.resizable(False, False)

    # Configure grid to center-align widgets
    root.grid_columnconfigure(0, weight=1)  # Center items in column 0
    root.grid_rowconfigure(0, weight=1)  # Add flexibility to rows for spacing

    frame = customtkinter.CTkFrame(root)
    frame.grid(row=0, column=0, padx=20, pady=60, sticky="nsew")  # Frame centered and expands

    # More flexibility to center within frame's grid
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_rowconfigure(0, weight=1)

    label = customtkinter.CTkLabel(frame, text="Shop Management DBMS", font=("Helvetica", 35))
    label.grid(row=0, column=0, padx=20, pady=20, sticky="n")  # Sticks to top center



    # Add entry button
    add_entry_btn = create_button(frame, text="Add Entry", command=lambda: show_entry_win(root))
    add_entry_btn.grid(row=2, column=0, padx=20, pady=10, sticky="n")  # Button centered

    # View entries button
    view_entry_btn = create_button(frame, text="View Entries", command=lambda: view_entries(root))
    view_entry_btn.grid(row=3, column=0, padx=20, pady=10, sticky="n")

    # Delete entries button
    clear_entries_btn = create_button(frame, text="Clear Entries", command=lambda: clear_entries(root))
    clear_entries_btn.grid(row=4, column=0, padx=20, pady=10, sticky="n")

    # Exit app button
    exit_btn = create_button(frame, text="Exit", command=lambda: confirm_user_exit(root))
    exit_btn.grid(row=5, column=0, padx=20, pady=10, sticky="n")

    root.mainloop()
