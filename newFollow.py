#! /usr/bin/python

# COMP 206 Assignment 4
# updateStatus.py
# Coded by Nicolas Velastegui
# ID: 260521419

# This script updates the follow-list of the currently logged-in user.
# It is similar in a lot of ways to the updateStatus.py script.

# We need to read the data from the POST form which comes as part of the stdin.
import os, sys, re

# --------------------------------------------------------------------------------
# READING INPUT DATA | Extracting username and newStalk --------------------------


# NAMES THAT ARE SUBSETS OF OTHER NAMES

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

# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------
# GENERATING LIST OF MEMBERS | Extracting list of members ------------------------
								#	As in MyFacebookPage.py

users = open("users.csv","r")
user_list = ""

for iteration in range(1,5000): # I suppose this means we have a maximum of 5000 users right now.
	current_line = users.readline() # Read the current line. 
	if current_line == "": # If it's empty, then we're at the end of the file.
		break
	# Instead of trying to extract the first part of the string (the username) we can
	# just set up a regex to remove everything after the first term.
	if iteration == 1:
		user_list = user_list + re.sub(',[\w\d\s,]*$','', current_line)
	else:
		user_list = user_list + ", " + re.sub(',[\w\d\s,]*$','', current_line)

users.close()

# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------
# TO APPEND, OR NOT TO APPEND | That is the question. ----------------------------
									# And by that I mean that now we either append
									# the proper changes or send the user to the
									# proper error page.

# With the input properly parsed, we have to appropriately append the users.csv file.

# Now there are probably hundreds of ways of doing this... but the method I decided on:

# 1. Scan the file for the line containing the user information.
# 2. Store this line in a string.
# 3. Delete the line from the file. (Using some str.sub-type method)
# 4. Add the newStalk to the end of the saved string (with the appropriate formatting).
# 5. Append the modified string to the end of the file.

# This works fine since we are using a simple linear search for the users.csv and topic.csv files.

# Using a modifed version of the method to find a specific line (from MyFacebookPage.py):
users = open("users.csv","r")
user_info = ""
for iteration in range(1,5000):
	current_line = users.readline() # Read the current line. 
	if current_line == "": # If it's empty, then we're at the end of the file.
		break
	if current_line.startswith(username): # username is the first value on each line.
		user_info = current_line
		break
users.close()

# House cleaning:
user_info = re.sub('\s$','',user_info)
# Just removing any spaces that may have been added at the end of the line.

# Now we can add the newStalk to the line... but ONLY if the user is not already following that other raccooner.

# In this first case, the user is already stalking newStalk, so we send them to a special page.
if newStalk in user_info:
	print "Content-Type:text/html;charset=iso-8859-1\n\n"
	print "<html>"
	print "<head>"
	print "<title>Error adding new stalk.</title>"
	print "</head>"
	print "<body bgcolor=\"black\">"
	print "<font color=\"white\" align=\"center\"><h1>Looks like you're already stalking " + newStalk + ".</h1></font>"
	print "<table>"
	print "<tr>"
	print "<td width=\"49%\">"
	print "</td>"
	print "<td>"
	# One of the best GIFs ever to appear on the Internet.
	print "<img align=\"middle\" src=\"http://31.media.tumblr.com/3d3fdf307ed0e67e1c2084e44b3607df/tumblr_myslquD2mj1sfpnpio1_400.gif\">"
	# Whole new meaning to 'Swiper, no swiping!'
	print "</td>"
	print "<td width=\"49%\">"
	print "</td>"
	print "</tr>"
	print "</table>"
	print "<font color=\"white\" align=\"center\"><h3>Bit too eager, maybe?</h3></font>"
	print "<font color=\"white\" align=\"center\"><h3>Press the button below to return to your feed bowl.</h3></font>"
	print "<form align=\"center\" action=\"MyFacebookPage.py\" method=\"post\">"
	print "<input type=\"hidden\" name=\"username\" value=\"" + username + "\">"
	print "<input type=\"submit\" value=\"To the feed bowl!\">"
	print "</form>"
	print "</body></html>"
	quit()
# In this second case, the newStalk inputted by the user does not exist.
# We direct the user to a different special page.
elif newStalk not in user_list:
	print "Content-Type:text/html;charset=iso-8859-1\n\n"
	print "<html>"
	print "<head>"
	print "<title>Error adding new stalk.</title>"
	print "</head>"
	print "<body bgcolor=\"black\">"
	print "<font color=\"white\" align=\"center\"><h1>The user " + newStalk + " does not exist on this server.</h1></font>"
	print "<table>"
	print "<tr>"
	print "<td width=\"49%\">"
	print "</td>"
	print "<td>"
	print "<img align=\"middle\" src=\"http://stanfordflipside.com/images/129raccoon.jpg\">"
	print "</td>"
	print "<td width=\"49%\">"
	print "</td>"
	print "</tr>"
	print "</table>"
	print "<font color=\"white\" align=\"center\"><h3>In the wrong trashcan, you are.</h3></font>"
	print "<font color=\"white\" align=\"center\"><h3>Press the button below to return to your feed bowl.</h3></font>"
	print "<form align=\"center\" action=\"MyFacebookPage.py\" method=\"post\">"
	print "<input type=\"hidden\" name=\"username\" value=\"" + username + "\">"
	print "<input type=\"submit\" value=\"To the feed bowl!\">"
	print "</form>"
	print "</body></html>"
	quit()

# If the above statements do not execute, then the script continues,
# and we must add the new user to the list of stalks...
# Now we have the original user line and the new user line.
new_user_info = user_info + ", " + newStalk

# Reopen the user file in read-mode and construct a set from all the lines in it.
users = open("users.csv","r")
users_lines = users.readlines()
users.close()

# Reopen the user file in write-mode and begin writing back the lines...
users = open("users.csv","w")
# We cycle through the list of lines that we took out before.
for current_line in users_lines:
	#current_line = re.sub('\s$','',current_line) # Remove any spaces that may have been added at the end of the line.
	if current_line.startswith(username):        # If there's a match between the current
	  									         # line and the copy we extracted previously...
		users.write(new_user_info)
		users.write('\n')
		continue # Then we break the loop and restart.
	users.write(current_line)
# At the end, we write the modified line.
# Notice that no line break is added.
# This is just due to the formatting of the file.
# Close the file.
users.close()

# With users.csv appended, we can generate the html page notifying the user.
# It also provides a link for the user to return to their feed bowl.

print "Content-Type:text/html;charset=iso-8859-1\n\n"
print "<html>"

print "<head>"
print "<title>New stalk added successfully!</title>"
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

print "<font color=\"white\"><h4>" + user_info + "</h4></font>"
print "<font color=\"white\"><h4>" + new_user_info + "</h4></font>"
print "<font color=\"white\"><h4>" + user_info + "</h4></font>"


print "</body></html>"