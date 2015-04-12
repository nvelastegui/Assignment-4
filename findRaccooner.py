# Then, to find a user again...
username = "Banana"
users_file = open("users.csv","r")
all_users = users_file.readlines()
users_file.close()
for line in all_users:
	if username in line:
		print line
		# Read line and sort data into... ________
