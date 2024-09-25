from customtkinter import *
from CTkMessagebox import CTkMessagebox


def create_button(master, text, command=None):
    return CTkButton(
        master,
        text=text,
        command=command,
        width=300,
        height=50,
        font=("Helvetica", 20)
    )


def create_label(master, text, font_size: int | None = 20):
    return CTkLabel(master, text=f"{text}", font=("Halvetica", font_size))


def create_entry(master, width: None | int = 140, height: None | int = 28, show: None | str = ''):
    if show is None or len(show) == 0:
        return CTkEntry(master, width=width, height=height)
    else:
        return CTkEntry(master, width=width, height=height, show=show)


def confirm_user_exit(master: CTk):
    confirm_request = CTkMessagebox(title="Exit", message="Do you want to close the app?", icon="question",
                                    option_3="Yes", option_1="Cancel", option_2="No")
    response = confirm_request.get()

    if response == "Yes":
        master.destroy()
    else:
        print("Click 'Yes' to exit!")
