import argparse
import requests
from user import user
from credentials import credentials
# User choose to login or create account
print("Welcome to password locker\n1. Login\n2.Signup")
parser = argparse.ArgumentParser()
parser.add_argument("choice", help="Choose")
args = parser.parse_args()

choice = args.choice

if(choice == 1):
	# Ask for the username and password
	username = input("Please enter you username")
	password = input("Please enter you password")

	# Check with the credentials class to authenticate
	loginStatus = credentials.login(username, password)

	if(loginStatus){

	}else{
		# Unsuccessful input
	}



parser = argparse.ArgumentParser()
parser.add_argument("username", help="Enter name")
parser.add_argument("password", help="Enter password")
args = parser.parse_args()

# C