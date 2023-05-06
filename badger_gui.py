import tkinter as tk
from tkinter import messagebox
from tkinter import Frame
from PIL import ImageTk, Image
import time
import subprocess

# Set global variables
local_path = "/home/user/Documents/Badger_2040/"
conference = "BSides Fort Wayne 2023"
badge_logo = "/badges/BadgeLogo.jpg"
badge_creator_logo = local_path + "BSidesLogo.png"
badge_file = local_path + "badge.txt"
badge_image = local_path + "BadgeLogo.jpg"
badge_script = local_path + "badge.py"
serial_port = "/dev/ttyACM0"

class BadgeForm:
    def __init__(self, master):
        self.master = master
        master.title("Badge Creator")
        master.attributes('-fullscreen',
                          True)

        # Add Event Title Label
        self.label_event = tk.Label(master, 
                                    text="BSides Fort Wayne 2023", 
                                    font=("Ariel",25))
        self.label_event.pack()

        # Add form Title Label
        self.label_title = tk.Label(master, 
                                    text="Badge Creator", 
                                    font=("Ariel",25))
        self.label_title.pack()

        # Load and resize the image
        self.image = ImageTk.PhotoImage(Image.open(badge_creator_logo).resize((446,278)))

        # Create a label for the image
        self.image_label = tk.Label(master, 
                                    image=self.image)
        self.image_label.pack()

        # Create a container frame for the fields
        self.field_container = tk.Frame(master)
        self.field_container.pack(padx=10, 
                                  pady=10)

        # Create a frame for the labels
        self.label_container = tk.Frame(self.field_container)
        self.label_container.pack(side=tk.LEFT)

        # Add Name Label
        self.label_name = tk.Label(self.label_container, 
                                   text="Name:", 
                                   font=("Ariel, 18"))
        self.label_name.grid(row=0, 
                             sticky='e')

        # Add Company Label
        self.label_company = tk.Label(self.label_container, 
                                      text="Company:", 
                                      font=("Ariel, 18"))
        self.label_company.grid(row=1, 
                                sticky='e')

        # Add Status Label
        self.label_status = tk.Label(self.label_container, 
                                     text="Status:", 
                                     font=("Ariel, 18"))
        self.label_status.grid(row=2, 
                               sticky='e')

        # Create a frame for the entry widgets
        self.entry_container = tk.Frame(self.field_container)
        self.entry_container.pack(side=tk.LEFT)

        # Add Entry for Name
        self.entry_name = tk.Entry(self.entry_container, 
                                   bd = 5)
        self.entry_name.grid(row=0, 
                             column=1)

        # Add Entry for Company
        self.entry_company = tk.Entry(self.entry_container, 
                                      bd = 5)
        self.entry_company.grid(row=1, 
                                column=1)

        # Add Dropdown for Status
        self.options = ["Attendee", 
                        "Sponsor", 
                        "Speaker", 
                        "Volunteer"]
        self.status_var = tk.StringVar()
        self.status_var.set(self.options[0])
        self.status_dropdown = tk.OptionMenu(self.entry_container, 
                                             self.status_var, 
                                             *self.options)
        self.status_dropdown.config(font=("Ariel",16))
        self.status_dropdown.grid(row=2, 
                                  column=1, 
                                  sticky='ew')
        
        # Set font for the Status dropdown
        self.status_menu = root.nametowidget(self.status_dropdown.menuname)
        self.status_menu.config(font=("Ariel",18))

        self.submit_button = tk.Button(master, 
                                       text="Create Badge", 
                                       command=self.create_badge, 
                                       width=30, 
                                       height=5, 
                                       bd=5, 
                                       font=("Ariel",18))
        self.submit_button.pack(pady=10)

    def create_badge(self):
        # Get the user input
        name = self.entry_name.get()
        company = self.entry_company.get()
        status = self.status_var.get()

        # Write the information to a file called badge.txt
        with open(badge, "w") as f:
            f.write(f"{status}\n{name}\n{company}\n\n{conference}\n\n{badge_logo}")

        # Wait for the Badger 2040 board to be ready
        time.sleep(2)

        # Transfer the files to the Badger 2040 board
        subprocess.run(['rshell', 
                        '-p', 
                        serial_port, 
                        'cp', 
                        badge_file, 
                        '/badges'])
        subprocess.run(['rshell', 
                        '-p', 
                        serial_port, 
                        'cp', 
                        badge_image, 
                        '/badges'])
        subprocess.run(['rshell', 
                        '-p', 
                        serial_port, 
                        'cp', 
                        badge_script, 
                        '/examples'])

        # Show a message box to confirm the badge was created
        messagebox.showinfo("Badge Created", 
                            "Badge has been created.")

        # Clear the form
        self.entry_name.delete(0, tk.END)
        self.entry_company.delete(0, tk.END)
        self.status_var.set("Attendee")

root = tk.Tk()

# Center grid
root.grid_rowconfigure(0, 
                       weight=1)
root.grid_columnconfigure(0, 
                          weight=1)
root.grid_rowconfigure(1, 
                       weight=1)
root.grid_columnconfigure(1, 
                          weight=1)
root.grid_rowconfigure(2, 
                       weight=1)
root.grid_rowconfigure(3, 
                       weight=1)

my_gui = BadgeForm(root)

# Run form until closed
root.mainloop()
