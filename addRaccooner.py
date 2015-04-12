# Script - Add a Raccooner.
# April 2 2015

# Basically, this has to take in three values:
# User's name
# Username
# Password
# No friends for now since this is a simple registration.

# Assuming that all values were appropriately passed:

name = "Sample Name"
username = "user_name"
password = "password"

# Need to open the csv file and append new user to line.
users_file = open("users.csv","a")
newline = name + "," + username + "," + password + "\n"
users_file.write(newline)
users_file.close()
