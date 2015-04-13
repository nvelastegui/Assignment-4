#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define FILENAME "../members.csv"



int main (void){
	printf("Content-type: text/html\n\n");
	printf("<html><head><title>Login</title></head><font face='Arial'><body>");

	char string[200];
	int i = 0;
	int size= atoi(getenv("CONTENT_LENGTH"));

//open desired file 
	FILE *data;
	data=fopen(FILENAME,"r");
	if (data==NULL)
		printf ("ERROR OPENING INPUT FILE");
	

//Variables used to read the users input 
	char username[200];
	char username2[200];
	char password[200];
	char line [200];
	
//Variables used to read the file 
	char fuser[200];
	char fname[200];
	char fpass[200];
	
//Get input (username and password)	
	fgets(string, size+1, stdin);


//knowing the first 9 characters are "username"
//Read the input by the user for usename
	i=9;
	while(string[i]!='&'){
		username[i-9]=string[i];
		username2[i-9]=string[i];
	i++;
	}
//Complete each String 
	username[i-9]=',';
	username2[i-9]='\0';//to display and pass to next Page
	username[i-8]='\0';//to compare with database

//Calculate index where password begins 	
	int usernameSize= strlen(username);
	int newStart= 9	+ usernameSize+9;

	i=newStart;
//Reading the password input by the user 
	while(i<size){
		password[i-newStart]=string[i];
		i++;
	}
//Complete the string 
	password[i-newStart]=',';
	password[i-newStart+1]='\0';
	
//Read the file 
	while(fgets(line, 200, data)!=NULL){
		sscanf(line, "%s %s %s", fuser, fname, fpass);
//		printf("<p>%s %s %s</p>", fuser, fname, fpass);//for testing 
//Validate the username and password match
		if(strcmp(fuser,username)==0 && strcmp(fpass, password)==0){
			printf("<p>");
			printf("Welcome back");
			printf("</p>");
	//Here goes the newsfeed 
			printf("<form name=\"reload\"  action=\"../MyFacebookPage.py\" method=\"post\">");
			printf("<input type=\"hidden\" name=\"username\" value=\"%s\">",username2);
			printf("<input type=\"submit\" value = \"Continue\">");
			printf("</form>");			

	//Close the file 
			fclose(data);
			printf("</body></font></html>");
			return 0;
		}
	}

//If no match was found then: 
	printf("<p>");	
	printf("The username and/or password are incorrect.\n");	
	printf("</p>");
	printf("<a href =../Welcome.html> Try again</a>");


	fclose(data);
	printf("</body></font></html>");
	return 1;	
}	




