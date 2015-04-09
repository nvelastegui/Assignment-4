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

username = re.sub('&[\d\w\s$-<>,?!\'.]*','',username) # remove all the junk from newStatus
username = re.sub('%[\d\w\s.]*','',username) # further cleaning since apostrophes and stuff are replaced by %number

# Conversion of some important characters that get changed during the post... 
# Definitely not all of them, but at this point I'm going to let it slide that
# some stuff will come out as %____
newStatus = re.sub('[\d\w\s$]*&','',newStatus)
newStatus = re.sub('%27','\'',newStatus)
newStatus = re.sub('%2C',',',newStatus)
newStatus = re.sub('%2F','/',newStatus)
newStatus = re.sub('%3F','?',newStatus)
newStatus = re.sub('%21','!',newStatus)
newStatus = re.sub('%3C','<',newStatus)
newStatus = re.sub('%3E','>',newStatus)
newStatus = re.sub('%3A',':',newStatus)
newStatus = re.sub('%3B',';',newStatus)
newStatus = re.sub('%22','\"',newStatus)
newStatus = re.sub('%5B','[',newStatus)
newStatus = re.sub('%5D',']',newStatus)
newStatus = re.sub('%7B','{',newStatus)
newStatus = re.sub('%7D','}',newStatus)
newStatus = re.sub('%2B','+',newStatus)
newStatus = re.sub('%3D','=',newStatus)
newStatus = re.sub('%28','(',newStatus)
newStatus = re.sub('%29',')',newStatus)

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
print "<title>Status updated successfully!</title>"
print "</head>"

# Generate the main portion of the page. Tell user the good news.
# Present funny gif image.
print "<body bgcolor=\"black\">"
print "<font color=\"white\" align=\"center\"><h1>Success!</h1></font>"

print "<table>"
print "<tr>"
print "<td width=\"49%\">"
print "</td>"
print "<td>"
print "<img align=\"middle\" src=\"http://www.strangezoo.com/images/content/133554.gif\">"
print "</td>"
print "<td width=\"49%\">"
print "</td>"
print "</tr>"
print "</table>"

print "<font color=\"white\" align=\"center\"><h3>" + username + ", your status was updated successfully.</h3></font>"
print "<font color=\"white\" align=\"center\"><h3>Press the button below to return to your feed bowl.</h3></font>"

# Create form for user to reload page. Uses post and a hidden tag.
print "<form align=\"center\" action=\"MyFacebookPage.py\" method=\"post\">"
print "<input type=\"hidden\" name=\"username\" value=\"" + username + "\">"
print "<input type=\"submit\" value=\"To the feed bowl!\">"
print "</form>"

print "</body></html>"

