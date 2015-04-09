#! /usr/bin/python

# COMP 206 Assignment 4
# updateStatus.py
# Coded by Nicolas Velastegui
# ID: 260521419

# This script updates the status of the currently logged-in user and
# generates the customized html page for the user's feed.

# We need to read the data from the POST form which comes as part of the stdin.
import os, sys, re

# Read the raw input from stdin
newStatus = sys.stdin.read()	# This contains something of the form:
								#	username=______&newStatus=_________

# Make it usable.
newStatus = re.sub('\+',' ',newStatus)
newStatus = re.sub('newStatus=','',newStatus)
newStatus = re.sub('username=','',newStatus)

# Split it into two strings.
# username and newStatus

username = newStatus

username = re.sub('&[\d\w\s.]*','',username)
newStatus = re.sub('[\d\w\s]*&','',newStatus)

# Input it into the database.

# Open the file, saved locally, with append mode.
topics = open("topic.csv","a")

# It took me a while to figure this out... I tried a number of different
# methods of printing to a file in Python. None of them seemed to work,
# and it had to do with formatting. Many methods didn't like my using of
# \n... but this simple method of file.writelines() seems to work perfectly.
topics.writelines('\n')
topics.writelines(username)
topics.writelines('\n')
topics.writelines(newStatus)

# Once data has been written, we can close the file.
topics.close()

# Below, a page is generated which confirms to the user that their status
# has been updated successfully. A link is provided to return to the home
# page. They will remain signed in.

print "Content-Type:text/html;charset=iso-8859-1\n\n"
print "<html>"

print "<head>"
print "<title>Raccooner - The Feed Bowl</title>"
print "</head>"

# -- Set the background colour to black.
print "<body bgcolor=\"black\">"
print "<font color=\"white\"><h2>" + username + "</h2></font>"
print "<font color=\"white\"><h2>" + newStatus + "</h2></font>"
print "</body></html>"

