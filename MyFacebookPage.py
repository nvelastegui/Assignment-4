#! /usr/bin/python

import sys
import re

# VARIABLES AND SUCH
username = "unholymist"

# --------------------------------------------------------------------------------
# USER DATABASE | Extracting List Of User's Friends-------------------------------

# First we need to open the users.csv file to find the line pertaining to the currently
# logged-in user.
users = open("users.csv","r")
user_friendlist = ""
for iteration in range(1,5000): # I suppose this means we have a maximum of 5000 users right now.
	current_line = users.readline() # Read the current line. 
	if current_line == "": # If it's empty, then we're at the end of the file.
		break
	if current_line.startswith(username): # username is the first value on each line.
		user_friendlist = current_line
		break
users.close()

# user_friendlist still has a lot of garbage attached to it
# (username, full name, and password) so we have to better format it

# We know the username, so we can easily remove it by using the strip function.
user_friendlist = user_friendlist.strip(username + ", ")

# However, we must now remove the full name and password from the string.
# We can use regular expressions for this, notably:
user_friendlist = re.sub('^\w*\s\w*, ','', user_friendlist)
# Matches: any combination of word characters followed by a single space or none then followed by any combination of word characters
# We do it again for the password:
user_friendlist = re.sub('^[\d\w]*, ','', user_friendlist)

# --------------------------------------------------------------------------------
# USER DATABASE | Extracting List Of All Members ---------------------------------

# In this case, we just need to take the first element from each line.
# We will cycle through is in the previous manner:
# (Notice I closed the file earlier. Now, reopening it will reset the
# position of the pointer in the file.)

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


# END USER DATABASE
# --------------------------------------------------------------------------------

# So to construct this script I first wrote out an html file for the general form,
# as recommended in the assignment sheet. I realize that instead of having a print for every
# line I could have had print """ """, which would have given more clarity to the html.
# However, I felt the method used below allowed me more freedom in inserting the 
# required user-specific values.

# The html can be seen easily in the included .html version of the feed page.

print "Content-Type:text/html;charset=iso-8859-1\n\n"
print "<html>"

# MyFacebookPage.py
# This script generates the customized html page for the user's feed.

# Remember: carry hidden tag from page to page.
print "<head>"
print "<title>Raccooner - The Feed Bowl</title>"
print "</head>"

# -- Set the background colour to black.
print "<body bgcolor=\"black\">"

# Main Feed Page

# -- For our headers, we should use a table. This is so that the greeting and the logo can be displayed on the same line
# -- but on opposite sides (ie. with opposite justifications)

# --------------------------------------------------------------------------------
# HEADER

print "<table width=\"100%\">" 

# One table row with greeting and site name.
print "<tr>"

# First column: "Hey, username."
print "<td align=\"left\" valign=\"top\" width=\"30%\">"
print "<font color=\"white\"><h1>Hey, " + username + ".</h1></font>" # adds the user's username to the header
print "</td>"

# Second column: Placeholder
print "<td>"
print "</td>"

# Third column: "Raccooner" + Refresh / Logout
# Note: refresh button is just for the retro-feel
print "<td valign=\"top\" width=\"30%\">"
print "<font color=\"white\" align=\"right\"><h1>Raccooner</h1></font>"
# Table for refresh and logout links
print "<table width=\"100%\">"
print "<tr>"
print "<td align=\"right\">"
print "<a href=\"http://google.ca\"><font color=\"white\">Refresh</font></a>"
print "</td>"
print "<td align=\"right\" width=\"50\">"
print "<a href=\"http://google.ca\"><font color=\"white\">Logout</font></a>"
print "</td>"
print "</tr>"
print "</table>"
print "</td>"
print "</tr>"
print "</table>"

# END OF HEADER
# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------
# NEWS FEED SECTION TITLE

print "<table width=\"100%\" bgcolor=\"gray\">"
print "<tr>"
print "<td width=\"25%\">"
print "</td>"
print "<td width=\"50%\" align=\"center\" bgcolor=\"gray\">"
print "<p><font color=\"white\" size=\"25\">The Feed Bowl</font></p>"
print "</td>"
print "<td width=\"25%\">"
print "</td>"
print "</tr>"
print "</table>"

# END OF NEWS FEED SECTION TITLE
# --------------------------------------------------------------------------------

# With the header done, we have to add the text box for the status update.

# --------------------------------------------------------------------------------
# STATUS BOX

print "<table width=\"100%\" cellspacing=\"20\" bgcolor=\"#959595\">"
print "<tr>"
print "<td width=\"25%\">"
print "</td>"
print "<td width=\"50%\" align=\"left\">"
print "<h2><font color=\"white\">Send a message:</font></h2>"

# SEND A STATUS FORM
print "<form name=\"statusUpdate\" action=\"MyFacebookPage.py\" method=\"get\">"
print "<input type=\"text\" name=\"newStatus\">"
print "<input type=\"submit\" value=\"Send it to the raccoon world!\">"
print "</form>"
# END OF NEW STATUS FORM
print "</td>"
print "<td width=\"25%\">"
print "</td>"
print "</tr>"
print "</table>"

# END OF STATUS BOX
# --------------------------------------------------------------------------------

# NEWS FEED (10 Entries)

print "<table width=\"100%\" cellspacing=\"20\" bgcolor=\"gray\">"
# The news feed is a table separated into 10 rows and 3 columns. The left and right
# columns are empty. The middle column displays a status update. The status
# updates are displayed from newest at the top to oldest at the bottom.

# Essentially, for this to work, the program must cycle through the topic.csv file
# and retract only the useful lines from it. ie. members of the user's friends list.
# We therefore require a string containing the names of all of the user's friends
# (which we created earlier).

# 10
# Each of these sections represents a table row.


# print "<tr>"
# print "<td width=\"25%\">"
# print "</td>"
# print "<td width=\"50%\">"
# print "<font color=\"white\"><h3 align=\"left\">" + current_user + " says:</h3></font>"
# print "<font color=\"white\"><p>"+ current_status + "</p></font>"
# print "</td>"
# print "<td width=\"25%\">"
# print "</td>"
# print "</tr>"

topics = open("topic.csv","r")

user_friendlist_merged = re.sub(', ','',user_friendlist)


current_user = ""
current_status = ""

status_count = 0 # Number of status updates already displayed.
#for number in range(1, 5000): # Similar to before, we will have a maximum number of statuses of 5000.

	#print "<tr><font color=\"white\">" + str(number) + "</font></tr>"

	# if status_count > 10:
	# 	break


	# if current_user == "":
	# 	break

current_user = topics.readline()
current_status = topics.readline()
current_user = re.sub('\s','',current_user)
print "<tr><font color=\"white\">" + current_user + current_status + "</font></tr>"

if current_user in user_friendlist_merged:
	print "<tr><font color=\"white\">word</font></tr>"
	# Print a new row with the appropriate columns.
	print "<tr><td width=\"25%\"></td><td width=\"50%\">"
	print "<font color=\"white\"><h3 align=\"left\">" + current_user + " says:</h3></font>"
	print "<font color=\"white\"><p>"+ current_status + "</p></font>"
	print "</td><td width=\"25%\"></td></tr>"
	status_count += 1
	print "<tr><font color=\"white\">" + str(status_count) + "</font></tr>"

current_user = topics.readline()
current_status = topics.readline()
current_user = re.sub('\s','',current_user)
print "<tr><font color=\"white\">" + current_user + current_status + "</font></tr>"

if current_user in user_friendlist_merged:
	print "<tr><font color=\"white\">word</font></tr>"
	# Print a new row with the appropriate columns.
	print "<tr><td width=\"25%\"></td><td width=\"50%\">"
	print "<font color=\"white\"><h3 align=\"left\">" + current_user + " says:</h3></font>"
	print "<font color=\"white\"><p>"+ current_status + "</p></font>"
	print "</td><td width=\"25%\"></td></tr>"
	status_count += 1
	print "<tr><font color=\"white\">" + str(status_count) + "</font></tr>"

current_user = topics.readline()
current_status = topics.readline()
current_user = re.sub('\s','',current_user)
print "<tr><font color=\"white\">" + current_user + current_status + "</font></tr>"

if current_user in user_friendlist_merged:
	print "<tr><font color=\"white\">word</font></tr>"
	# Print a new row with the appropriate columns.
	print "<tr><td width=\"25%\"></td><td width=\"50%\">"
	print "<font color=\"white\"><h3 align=\"left\">" + current_user + " says:</h3></font>"
	print "<font color=\"white\"><p>"+ current_status + "</p></font>"
	print "</td><td width=\"25%\"></td></tr>"
	status_count += 1
	print "<tr><font color=\"white\">" + str(status_count) + "</font></tr>"

current_user = topics.readline()
current_status = topics.readline()
current_user = re.sub('\s','',current_user)
print "<tr><font color=\"white\">" + current_user + current_status + "</font></tr>"

if current_user in user_friendlist_merged:
	print "<tr><font color=\"white\">word</font></tr>"
	# Print a new row with the appropriate columns.
	print "<tr><td width=\"25%\"></td><td width=\"50%\">"
	print "<font color=\"white\"><h3 align=\"left\">" + current_user + " says:</h3></font>"
	print "<font color=\"white\"><p>"+ current_status + "</p></font>"
	print "</td><td width=\"25%\"></td></tr>"
	status_count += 1
	print "<tr><font color=\"white\">" + str(status_count) + "</font></tr>"

current_user = topics.readline()
current_status = topics.readline()
current_user = re.sub('\s','',current_user)
	#print "<tr><font color=\"white\">" + current_user + current_status + "</font></tr>"

if current_user in user_friendlist_merged:
	print "<tr><font color=\"white\">word</font></tr>"
	# Print a new row with the appropriate columns.
	print "<tr><td width=\"25%\"></td><td width=\"50%\">"
	print "<font color=\"white\"><h3 align=\"left\">" + current_user + " says:</h3></font>"
	print "<font color=\"white\"><p>"+ current_status + "</p></font>"
	print "</td><td width=\"25%\"></td></tr>"
	status_count += 1
	print "<tr><font color=\"white\">" + str(status_count) + "</font></tr>"

topics.close()


# # 9
# print "<tr>"
# print "<td width=\"25%\">"
# print "</td>"
# print "<td width=\"50%\">"
# print "<font color=\"white\"><h3 align=\"left\">User_1 says:</h3></font>"
# print "<font color=\"white\"><p>This is a new line.</p></font>"
# print "</td>"
# print "<td width=\"25%\">"
# print "</td>"
# print "</tr>"

# # 8
# print "<tr>"
# print "<td width=\"25%\">"
# print "</td>"
# print "<td width=\"50%\">"
# print "<font color=\"white\"><h3 align=\"left\">User_1 says:</h3></font>"
# print "<font color=\"white\"><p>Raccoons be cool, yo.</p></font>"
# print "</td>"
# print "<td width=\"25%\">"
# print "</td>"
# print "</tr>"

# # 7
# print "<tr>"
# print "<td width=\"25%\">"
# print "</td>"
# print "<td width=\"50%\">"
# print "<font color=\"white\"><h3 align=\"left\">User_1 says:</h3></font>"
# print "<font color=\"white\"><p>Raccoons be cool, yo.</p></font>"
# print "</td>"
# print "<td width=\"25%\">"
# print "</td>"
# print "</tr>"

# # 6
# print "<tr>"
# print "<td width=\"25%\">"
# print "</td>"
# print "<td width=\"50%\">"
# print "<font color=\"white\"><h3 align=\"left\">User_1 says:</h3></font>"
# print "<font color=\"white\"><p>Raccoons be cool, yo.</p></font>"
# print "</td>"
# print "<td width=\"25%\">"
# print "</td>"
# print "</tr>"

# # 5
# print "<tr>"
# print "<td width=\"25%\">"
# print "</td>"
# print "<td width=\"50%\">"
# print "<font color=\"white\"><h3 align=\"left\">User_1 says:</h3></font>"
# print "<font color=\"white\"><p>Raccoons be cool, yo.</p></font>"
# print "</td>"
# print "<td width=\"25%\">"
# print "</td>"
# print "</tr>"

# # 4
# print "<tr>"
# print "<td width=\"25%\">"
# print "</td>"
# print "<td width=\"50%\">"
# print "<font color=\"white\"><h3 align=\"left\">User_1 says:</h3></font>"
# print "<font color=\"white\"><p>Raccoons be cool, yo.</p></font>"
# print "</td>"
# print "<td width=\"25%\">"
# print "</td>"
# print "</tr>"

# # 3
# print "<tr>"
# print "<td width=\"25%\">"
# print "</td>"
# print "<td width=\"50%\">"
# print "<font color=\"white\"><h3 align=\"left\">User_1 says:</h3></font>"
# print "<font color=\"white\"><p>Raccoons be cool, yo.</p></font>"
# print "</td>"
# print "<td width=\"25%\">"
# print "</td>"
# print "</tr>"

# # 2
# print "<tr>"
# print "<td width=\"25%\">"
# print "</td>"
# print "<td width=\"50%\">"
# print "<font color=\"white\"><h3 align=\"left\">User_1 says:</h3></font>"
# print "<font color=\"white\"><p>Raccoons be cool, yo.</p></font>"
# print "</td>"
# print "<td width=\"25%\">"
# print "</td>"
# print "</tr>"

# # 1
# print "<tr>"
# print "<td width=\"25%\">"
# print "</td>"
# print "<td width=\"50%\">"
# print "<font color=\"white\"><h3 align=\"left\">User_1 says:</h3></font>"
# print "<font color=\"white\"><p>Raccoons be cool, yo.</p></font>"
# print "</td>"
# print "<td width=\"25%\">"
# print "</td>"
# print "</tr>"

# End table
print "</table>"

# END OF NEWS FEED
# --------------------------------------------------------------------------------

# At the bottom of the news feed, we have to present the user with the usernames of all other members of the network.
# Again, we will use a table, to ensure that the text is properly centered.

# --------------------------------------------------------------------------------
# OTHER RACCOONERS
print "<table width=\"100%\" cellspacing=\"20\" bgcolor=\"#959595\">" # Begin Table For Section

# All Members Of Raccooner.
print "<tr>"
print "</tr>"
print "<tr>"
print "<td width=\"25%\">"
print "</td>"

print "<td width=\"50%\" align=\"left\" valign=\"middle\">"
print "<font color=\"white\"><h2>Other Raccooners</h2></font>"
print "<font color=\"white\"><p>" + user_list +"</p></font>"
print "</td>"

print "<td width=\"25%\">"
print "</td>"
print "</tr>"

# User's Friends.
# (Using previously created user_friendlist)
print "<tr>"
print "</tr>"
print "<tr>"
print "<td width=\"25%\">"
print "</td>"

print "<td width=\"50%\" align=\"left\" valign=\"middle\">"
print "<font color=\"white\"><h2>" + username + "\'s Friends</h2></font>"
print "<font color=\"white\"><p>" + user_friendlist + "</p></font>"
print "</td>"

print "<td width=\"25%\">"
print "</td>"
print "</tr>"

print "</table>" # End Table For Section

# Add a member to your friendlist section
print "<table width=\"100%\" cellspacing=\"20\" bgcolor=\"#959595\">"
print "<tr>"
print "<td width=\"25%\">"
print "</td>"
print "<td width=\"50%\" align=\"left\">"
print "<h3><font color=\"white\">Stalk a fellow raccooner:</font></h3>"
print "<form name=\"CoonUpdate\" method=\"post\">"
print "<input type=\"text\" name=\"newStalk\">"
print "<input type=\"submit\" value=\"Stalk\">"
print "</form>"
print "</td>"
print "<td width=\"25%\">"
print "</td>"
print "</tr>"
print "</table>"

# End Of Body
# and End of HTML
# for testing
print "</body>"
print "</html>"

