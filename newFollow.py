#! /usr/bin/python

# COMP 206 Assignment 4
# updateStatus.py
# Coded by Nicolas Velastegui
# ID: 260521419

# This script updates the follow-list of the currently logged-in user.
# It is similar in a lot of ways to the updateStatus.py script.

# We need to read the data from the POST form which comes as part of the stdin.
import os, sys, re

# Read the raw input from stdin
newStalk = sys.stdin.read()	# This contains something of the form:
							#	username=______&newStalk=_________

# Make it usable.
newStalk = re.sub('\+',' ',newStalk)
newStalk = re.sub('newStalk=','',newStalk)
newStalk = re.sub('username=','',newStalk)
# At this point only seperated by &.
# Split it into two strings.
# username and newStalk
username = newStalk

username = re.sub('&[\d\w\s$-<>,?!\'.]*','',username) # remove all the junk from newStalk
username = re.sub('%[\d\w\s.]*','',username) # Not necessarily needed in this script since usernames don't contain these characters, but good for safety anyway.

newStalk = re.sub('[\d\w\s$]*&','',newStalk)

# With the input properly parsed, we have to appropriately append the users.csv file.

# Insert dat code here

# With users.csv appended, we can generate the html page notifying the user.
# It also provides a link for the user to return to their feed bowl.

print "Content-Type:text/html;charset=iso-8859-1\n\n"
print "<html>"

print "<head>"
print "<title>Status updated successfully!</title>"
print "</head>"

# Generate the main portion of the page. Tell user the good news.
# Present funny gif image.
print "<body bgcolor=\"black\">"
print "<font color=\"white\" align=\"center\"><h1>Congratulations on the new stalk!</h1></font>"

print "<table>"
print "<tr>"
print "<td width=\"49%\">"
print "</td>"
print "<td>"
print "<img align=\"middle\" src=\"http://www.sciencebuzz.org/sites/default/files/images/raccoons_dark.jpg\">"
print "</td>"
print "<td width=\"49%\">"
print "</td>"
print "</tr>"
print "</table>"

print "<font color=\"white\" align=\"center\"><h3>" + username + ", you are now stalking " + newStalk + ".</h3></font>"
print "<font color=\"white\" align=\"center\"><h3>Press the button below to return to your feed bowl.</h3></font>"

# Create form for user to reload page. Uses post and a hidden tag.
print "<form align=\"center\" action=\"MyFacebookPage.py\" method=\"post\">"
print "<input type=\"hidden\" name=\"username\" value=\"" + username + "\">"
print "<input type=\"submit\" value=\"To the feed bowl!\">"
print "</form>"

print "</body></html>"