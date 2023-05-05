import tkinter as tk
from tkinter import messagebox
import os
import time
import subprocess

class BadgeForm:
    def __init__(self, master):
        self.master = master
        master.title("Badge Creator")
        master.attributes('-fullscreen',True)

        #getting screen width and height of display
        #width= master.winfo_screenwidth()
        #height= master.winfo_screenheight()
        #setting tkinter window size
        #master.geometry("%dx%d" % (width, height))

        self.label_name = tk.Label(master, text="Name")
        self.label_name.grid(row=0, sticky='ne')

        self.label_company = tk.Label(master, text="Company")
        self.label_company.grid(row=1, sticky='ne', padx=10, pady=0)

        self.label_status = tk.Label(master, text="Status")
        self.label_status.grid(row=2, sticky='ne', padx=10, pady=0)

        self.entry_name = tk.Entry(master)
        self.entry_name.grid(row=0, column=1, sticky='nw', padx=10, pady=0)

        self.entry_company = tk.Entry(master)
        self.entry_company.grid(row=1, column=1, sticky='nw', padx=10, pady=0)

        self.options = ["Attendee", "Sponsor", "Speaker", "Volunteer"]
        self.status_var = tk.StringVar()
        self.status_var.set(self.options[0])
        self.status_dropdown = tk.OptionMenu(master, self.status_var, *self.options)
        self.status_dropdown.grid(row=2, column=1, sticky='nw', padx=10, pady=0)

        self.submit_button = tk.Button(master, text="Create Badge", command=self.create_badge)
        self.submit_button.grid(row=3, columnspan=2, sticky='n', padx=10, pady=0)

        self.space1 = tk.Label(master, height=1)
        self.space1.grid(row=4, columnspan=2, sticky='')

        self.space2 = tk.Label(master, height=1)
        self.space2.grid(row=5, columnspan=2, sticky='')

        self.space3 = tk.Label(master, height=1)
        self.space3.grid(row=6, columnspan=2, sticky='')

        self.space4 = tk.Label(master, height=1)
        self.space4.grid(row=7, columnspan=2, sticky='')

        self.space5 = tk.Label(master, height=1)
        self.space5.grid(row=8, columnspan=2, sticky='')

        self.space6 = tk.Label(master, height=1)
        self.space6.grid(row=9, columnspan=2, sticky='')

        self.space7 = tk.Label(master, height=1)
        self.space7.grid(row=10, columnspan=2, sticky='')

        self.space8 = tk.Label(master, height=1)
        self.space8.grid(row=11, columnspan=2, sticky='')

        self.space9 = tk.Label(master, height=1)
        self.space9.grid(row=12, columnspan=2, sticky='')

        self.space10 = tk.Label(master, height=1)
        self.space10.grid(row=13, columnspan=2, sticky='')

        self.space11 = tk.Label(master, height=1)
        self.space11.grid(row=14, columnspan=2, sticky='')

        self.space12 = tk.Label(master, height=1)
        self.space12.grid(row=15, columnspan=2, sticky='')

        self.space13 = tk.Label(master, height=1)
        self.space13.grid(row=16, columnspan=2, sticky='')

        self.space14 = tk.Label(master, height=1)
        self.space14.grid(row=17, columnspan=2, sticky='')

        self.space15 = tk.Label(master, height=1)
        self.space15.grid(row=18, columnspan=2, sticky='')

        self.space16 = tk.Label(master, height=1)
        self.space16.grid(row=19, columnspan=2, sticky='')

        self.space17 = tk.Label(master, height=1)
        self.space17.grid(row=20, columnspan=2, sticky='')

        self.space18 = tk.Label(master, height=1)
        self.space18.grid(row=21, columnspan=2, sticky='')

        self.space19 = tk.Label(master, height=1)
        self.space19.grid(row=22, columnspan=2, sticky='')

    def create_badge(self):
        # Get the user input
        name = self.entry_name.get()
        company = self.entry_company.get()
        status = self.status_var.get()

        # Set other variables
        conference = "BSides Fort Wayne 2023"
        picture = "/badges/BadgeLogo.jpg"
        badge = "/home/user/Documents/Badger_2040/badge.txt"
        image = "/home/user/Documents/Badger_2040/BadgeLogo.jpg"
        badge_script = "/home/user/Documents/Badger_2040/badge.py"
        serial_port = "/dev/ttyACM0"

        # Write the information to a file called badge.txt
        with open(badge, "w") as f:
            f.write(f"{status}\n{name}\n{company}\n\n{conference}\n\n{picture}")

        # Wait for the Badger 2040 board to be ready
        time.sleep(2)

        # Transfer the files to the Badger 2040 board
        subprocess.run(['rshell', '-p', serial_port, 'cp', badge, '/badges'])
        subprocess.run(['rshell', '-p', serial_port, 'cp', image, '/badges'])
        subprocess.run(['rshell', '-p', serial_port, 'cp', badge_script, '/examples'])

        # Show a message box to confirm the badge was created
        messagebox.showinfo("Badge Created", "Badge has been created.")

        # Clear the form
        self.entry_name.delete(0, tk.END)
        self.entry_company.delete(0, tk.END)
        self.status_var.set("Attendee")

root = tk.Tk()
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
my_gui = BadgeForm(root)
root.mainloop()
