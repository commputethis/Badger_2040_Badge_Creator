import argparse
import os
import time
import subprocess

# Create an ArgumentParser object
parser = argparse.ArgumentParser()

# Add command-line arguments for name, company, and title
parser.add_argument("--name", help="Your name", default=" ")
parser.add_argument("--company", help="Your company", default=" ")
parser.add_argument("--title", help="Your job title", default="Attendee")

# Parse the command-line arguments
args = parser.parse_args()

# Set other variables
conference = "BSides Fort Wayne 2023"
picture = "/badges/BadgeLogo.jpg"
badge = "/home/user/badge.txt"
image = "/home/user/BadgeLogo.jpg"
badge_script = "/home/user/badge.py"
serial_port = "/dev/ttyACM0"

# Write the information to a file called badge.txt
with open(badge, "w") as f:
    f.write(f"{args.title}\n{args.name}\n{args.company}\n\n{conference}\n\n{picture}")

# Wait for the Badger 2040 board to be ready
time.sleep(2)

# Transfer the files to the Badger 2040 board
subprocess.run(['rshell', '-p', serial_port, 'cp', badge, '/badges'])
subprocess.run(['rshell', '-p', serial_port, 'cp', image, '/badges'])
subprocess.run(['rshell', '-p', serial_port, 'cp', badge_script, '/examples'])
