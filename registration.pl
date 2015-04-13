#! /usr/bin/perl -wT
use strict;
use CGI':standard';
use warnings;


print "Content-type:text/html\r\n\r\n";

#parse in name, username and password
my $name = param('name');
my $username = param ('username');
my $password = param('password');
my $friends = " ";

#boolean is true when no other username exists that matches what was entered
my $boolean = 0;

#read from csv file to validate username
open (ReadFILE, '< members.csv') or $boolean = 'true';
#read line by line, parse string into words, compare usernames in the csv to the username entered, if there is duplicate, then set boolean to false
while (my $line = <ReadFILE>)
{
	
        my @word = split/,/,$line;
	if (($username eq "")||($name eq "") || ($password eq ""))
	{
		$boolean = 2;
		last;
	}
	elsif ($word[0] eq "$username")
        {
                $boolean = 1;
        }
	else
	{
		$boolean = 0;
	}
}

if ($boolean == 2)
{
	my $htmlF = qq{
        <html>
        <head>
                <title>Fail to register</title>
        </head>
        <body>
                <img src="Image/jpg/LOGO1.jpg" width="20%" height="auto">
                <table align="right" cellspacing="40x">
                        <tr>
                                <td width="50%">
                                        <h1><b>Registration Failed<b><h1>
                                        <p>Please do not leave blank</p>
                                        <h2><a href="registrationHTML.html" target="_self">Try Again</a></h2>
                                </td>
                                <td width="50%"><img src="Image/jpg/Sorry.jpg" width="75%" height="auto"></td>
                        </tr>
                </table>
        </body>
        </html>};
        print $htmlF;

}
#when boolena is false, display error message and a link back to the login page
elsif($boolean == 1)
{
	my $htmlF = qq{
	<html>
	<head>
		<title>Fail to register</title>
	</head>
	<body>
		<img src="Image/jpg/LOGO1.jpg" width="20%" height="auto">
		<table align="right" cellspacing="40x">
			<tr>
				<td width="50%">
					<h1><b>Registration Failed<b><h1>
					<p>username already existed</p>
					<h2><a href="registrationHTML.html" target="_self">Try Again</a></h2>
				</td>
				<td width="50%"><img src="Image/jpg/Sorry.jpg" width="75%" height="auto"></td>
			</tr>
		</table>
	</body>
	</html>};
	print $htmlF;
	
}
#when boolean is true, append the information to the csv, display congratulation page and a link back to the welcome page
else
{
	$name =~ s/ /+/g;	
	open (AppendFILE,'>>members.csv');
	print AppendFILE "$username, $name, $password, $friends \n";
	close (AppendFILE);

	my $htmlS = qq{
	<html>
	<head>
		<title>Congratulations</title>
	</head>
	<body>
		<img src="Image/jpg/LOGO1.jpg" width="20%" height="auto">
		<table align="right" cellspacing="40x">
			<tr>
				<td width="40%">
					<br><br><h3 align="center">ACCEPTANCE LETTER</h3><br>
					<p>Dear $username,</p>
					<p><b>Congratulations!</b> It is my pleasure to offer you admission at Raccooner. This opportunity to join one of the most outstanding raccoon bodies in the country comes in recognition of your academic and personal achievements. I and the other members of the Admission Committee know that you would be a valued member of raccooner both in and out of den.</p>
					<p>On behalf of all of us who had the pleasure of reviewing your application, best wishes to you for a successful and enjoyable future.</p>
					<p>Sincerely,</p>
					<p>Racconner Committe</p>
					<p>Dean of Admission</p><br>
					<h2>Ready to Coon? <a href="Welcome.html" target="_self"> Login</a></h2>
				</td>
				<td width="60%"><img src="Image/jpg/Congratulations.jpg" width="100%" height="auto"></td>
			</tr>
		</table>
	</body>
</html>};
	print $htmlS;
	
}


