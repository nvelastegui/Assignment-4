#! /usr/bin/python

print "Content-Type:text/html;charset=iso-8859-1\n\n"
print "<html>"

# MyFacebookPage.py
# This script generates the customized html page for the user's feed.

# Remember: carry hidden tag from page to page.
print "<head>"
print "<title>Raccooner - The Feed Bowl</title>"
print "</head>"

# -- Set the background colour to black. -->
print "<body bgcolor=\"black\">"

# -- Main Feed Page -->

# -- For our headers, we should use a table. This is so that the greeting and the logo can be displayed on the same line -->
# -- but on opposite sides (ie. with opposite justifications) -->

# -- ____________________________________________________________________________________________________________________ -->

# -- Header -->

print "<table width=\"100%\">" 

# One table row with greeting and site name. -->
print "<tr>"

# First column: "Hey, username." -->
print "<td align=\"left\" valign=\"top\" width=\"30%\">"
print "<font color=\"white\"><h1>Hey, username.</h1></font>"
print "</td>"

# Second column: Placeholder -->
print "<td>"
print "</td>"

# Third column: "Raccooner" + Refresh / Logout -->
# Note: refresh button is just for the retro-feel -->
print "<td valign=\"top\" width=\"30%\">"
print "<font color=\"white\" align=\"right\"><h1>Raccooner</h1></font>"
# Table for refresh and logout links -->
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

# End of Header -->

# ____________________________________________________________________________________________________________________ -->

# News Feed Section Title -->

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

# End of News Feed Section Title -->

# End Of Body
# and End of HTML
# for testing
print "</body>"
print "</html>"