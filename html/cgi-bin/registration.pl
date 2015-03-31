#! /usr/bin/perl -wT
use strict;
use CGI':standard';

print "Content-Type: text/html\n\n";

my $name = param('name');
my $usrname = param ('usrname');
my $password = param('password');

my $OPEN=open (FILE,'>>members.csv');
print $name;
print $usrname;
print $password;
close (FILE);


