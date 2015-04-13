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
	FILE *data;
	data=fopen(FILENAME,"r");
	if (data==NULL)
		printf ("ERROR OPENING INPUT FILE");
	

	char username[200];
	char username2[200];
	char password[200];
	
	char fuser[200];
	char fname[200];
	char fpass[200];
	
	
	fgets(string, size+1, stdin);
//	printf("<p>");
//	printf("%s", string);
//	printf("</p>");
//	printf("<p>");
//	printf("%d", size);
//	printf("</p>");	

	i=9;
	while(string[i]!='&'){
//		if(string[i]!='+'){
		username[i-9]=string[i];
		username2[i-9]=string[i];
//		}
//		else
//			username[i-9]=' ';
	i++;
	}
	username[i-9]=',';
	username2[i-9]='\0';
	username[i-8]='\0';
//	printf("<p>");
//	printf("%s",username2);
//	printf("</p>");
	
	int usernameSize= strlen(username);
	int newStart= 9	+ usernameSize+9;

	i=newStart;
	while(i<size){
//		if(string[i]!='+')
			password[i-newStart]=string[i];
//		else
//			password[i-newStart]=' ';
	i++;
	}
	password[i-newStart]=',';
	password[i-newStart+1]='\0';
//	printf("<p>");
//	printf("%d,%s",i,  password);
//	printf("</p>");
	while((fscanf(data, "%s %s %s", fuser, fname, fpass))==3){
//		printf("<p>%s %s %s</p>", fuser, fname, fpass);
		if(strcmp(fuser,username)==0 && strcmp(fpass, password)==0){
			printf("<p>");
			printf("Welcome back");
			printf("</p>");
			//Here goes the newsfeed 
//			printf("<a href =../feedbowl.html> Continue... --> </a>");
			printf("<form name=\"reload\"  action=\"../MyFacebookPage.py\" method=\"post\">");
			printf("<input type=\"hidden\" name=\"username\" value=\"%s\">",username2);
			printf("<input type=\"submit\" value = \"Continue\">");
			printf("</form>");			


			fclose(data);
			printf("</body></font></html>");
			return 0;
		}
	}

	printf("<p>");	
	printf("The username and/or password are incorrect.\n");	
	printf("</p>");
	printf("<a href =../Welcome.html> Try again</a>");


	fclose(data);
	printf("</body></font></html>");
	return 1;	
}	




