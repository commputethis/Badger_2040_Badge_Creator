import os
import time
import subprocess

# Prompt the user for their name and company
name = input("Enter your name: ")
company = input("Enter your company: ")

# Set other variables
conference = "BSides Fort Wayne 2023"
designation = "Attendee"
picture = "/badges/BadgeLogo.jpg"
badge = "/home/dprows/badge.txt"
image = "/home/dprows/BadgeLogo.jpg"
badge_script = "/home/dprows/badge.py"
serial_port = "/dev/ttyACM0"

# Write the information to a file called badge.txt
with open(badge, "w") as f:
    f.write(f"{designation}\n{name}\n{company}\n\n{conference}\n\n{picture}")

# Wait for the Badger 2040 board to be ready
time.sleep(2)

# Transfer the files to the Badger 2040 board
subprocess.run(['rshell', '-p', serial_port, 'cp', badge, '/badges'])
subprocess.run(['rshell', '-p', serial_port, 'cp', image, '/badges'])
subprocess.run(['rshell', '-p', serial_port, 'cp', badge_script, '/examples'])
