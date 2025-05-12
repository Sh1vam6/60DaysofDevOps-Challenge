#!/bin/bash


# Automate user account creation – Write a script that takes the username as an argument, checks,
#  if the user exists, gives the message “user already exists“ else creates a new user,
#   adds it to a “devops“ group, and sets up a default home directory.


if [ $# -eq 0 ]; then
	echo "provide username as argument"
	exit 1
fi

USERNAME="$1"
GROUP="devops"

# checking existance of user
if id $USERNAME &>/dev/null; then
	echo "$USERNAME already exits"
else 
	# create the group if dosen't exist
	if ! getent group "GROUP"  &>/dev/null; then
		sudo groupadd $GROUP
	fi
        
	# creating user with home dir and adding to a group
	echo "creating $USERNAME ..."
	sudo useradd -m -s /bin/bash -G "$GROUP" "$USERNAME"
        # Set a default password (optional, force change on first login)
        echo "$USERNAME:ChangeMe123" | sudo chpasswd
        sudo passwd --expire "$USERNAME"
fi
