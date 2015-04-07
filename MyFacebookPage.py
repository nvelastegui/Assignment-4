#! /usr/bin/python

# VARIABLES AND SUCH
username = "unholymist"
name = "Nicolas Velastegui"
password = "password"

# --------------------------------------------------------------------------------
# STATUS DATABASE ----------------------------------------------------------------

topics = open("topic.csv","r")
topics.close()

# END STATUS DATABASE
# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------
# USER DATABASE ------------------------------------------------------------------

users = open("users.csv","r")
users.close()

# END USER DATABASE
# --------------------------------------------------------------------------------

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
print "<font color=\"white\"><h1>Hey, " + username + ".</h1></font>"
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
# The news feed is a table separated into 10 rows and 3 columns. The left and right columns are empty.
# The middle column displays a coon (a status update). The status updates are displayed from newest at the top
# to oldest at the bottom.

# 10
print "<tr>"
print "<td width=\"25%\">"
print "</td>"
print "<td width=\"50%\">"
print "<font color=\"white\"><h3 align=\"left\">User_1 says:</h3></font>"
print "<font color=\"white\"><p>The raccoon, sometimes spelled racoon, also known as the common raccoon, North American raccoon, northern raccoon and colloquially as coon, is a medium-sized mammal native to North America.</p></font>"
print "</td>"
print "<td width=\"25%\">"
print "</td>"
print "</tr>"

# 9
print "<tr>"
print "<td width=\"25%\">"
print "</td>"
print "<td width=\"50%\">"
print "<font color=\"white\"><h3 align=\"left\">User_1 says:</h3></font>"
print "<font color=\"white\"><p>This is a new line.</p></font>"
print "</td>"
print "<td width=\"25%\">"
print "</td>"
print "</tr>"

# 8
print "<tr>"
print "<td width=\"25%\">"
print "</td>"
print "<td width=\"50%\">"
print "<font color=\"white\"><h3 align=\"left\">User_1 says:</h3></font>"
print "<font color=\"white\"><p>Raccoons be cool, yo.</p></font>"
print "</td>"
print "<td width=\"25%\">"
print "</td>"
print "</tr>"

# 7
print "<tr>"
print "<td width=\"25%\">"
print "</td>"
print "<td width=\"50%\">"
print "<font color=\"white\"><h3 align=\"left\">User_1 says:</h3></font>"
print "<font color=\"white\"><p>Raccoons be cool, yo.</p></font>"
print "</td>"
print "<td width=\"25%\">"
print "</td>"
print "</tr>"

# 6
print "<tr>"
print "<td width=\"25%\">"
print "</td>"
print "<td width=\"50%\">"
print "<font color=\"white\"><h3 align=\"left\">User_1 says:</h3></font>"
print "<font color=\"white\"><p>Raccoons be cool, yo.</p></font>"
print "</td>"
print "<td width=\"25%\">"
print "</td>"
print "</tr>"

# 5
print "<tr>"
print "<td width=\"25%\">"
print "</td>"
print "<td width=\"50%\">"
print "<font color=\"white\"><h3 align=\"left\">User_1 says:</h3></font>"
print "<font color=\"white\"><p>Raccoons be cool, yo.</p></font>"
print "</td>"
print "<td width=\"25%\">"
print "</td>"
print "</tr>"

# 4
print "<tr>"
print "<td width=\"25%\">"
print "</td>"
print "<td width=\"50%\">"
print "<font color=\"white\"><h3 align=\"left\">User_1 says:</h3></font>"
print "<font color=\"white\"><p>Raccoons be cool, yo.</p></font>"
print "</td>"
print "<td width=\"25%\">"
print "</td>"
print "</tr>"

# 3
print "<tr>"
print "<td width=\"25%\">"
print "</td>"
print "<td width=\"50%\">"
print "<font color=\"white\"><h3 align=\"left\">User_1 says:</h3></font>"
print "<font color=\"white\"><p>Raccoons be cool, yo.</p></font>"
print "</td>"
print "<td width=\"25%\">"
print "</td>"
print "</tr>"

# 2
print "<tr>"
print "<td width=\"25%\">"
print "</td>"
print "<td width=\"50%\">"
print "<font color=\"white\"><h3 align=\"left\">User_1 says:</h3></font>"
print "<font color=\"white\"><p>Raccoons be cool, yo.</p></font>"
print "</td>"
print "<td width=\"25%\">"
print "</td>"
print "</tr>"

# 1
print "<tr>"
print "<td width=\"25%\">"
print "</td>"
print "<td width=\"50%\">"
print "<font color=\"white\"><h3 align=\"left\">User_1 says:</h3></font>"
print "<font color=\"white\"><p>Raccoons be cool, yo.</p></font>"
print "</td>"
print "<td width=\"25%\">"
print "</td>"
print "</tr>"

# End table
print "</table>"

# END OF NEWS FEED
# --------------------------------------------------------------------------------

# At the bottom of the news feed, we have to present the user with the usernames of all other members of the network.
# Again, we will use a table, to ensure that the text is properly centered.

# --------------------------------------------------------------------------------
# OTHER RACCOONERS
print "<table width=\"100%\" bgcolor=\"#959595\">"
print "<tr>"
print "</tr>"
print "<tr>"
print "<td width=\"25%\">"
print "</td>"

print "<td width=\"50%\" align=\"center\" valign=\"middle\">"
print "<font color=\"white\"><h2>Other Raccooners</h2></font>"
print "<font color=\"white\"><p>Coontastic TheCoonster CooningTime</p></font>"
print "</td>"

print "<td width=\"25%\">"
print "</td>"
print "</tr>"
print "</table>"

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

print  "<p><font color=\"white\">" + all_topics + "</font></p>"

# End Of Body
# and End of HTML
# for testing
print "</body>"
print "</html>"

