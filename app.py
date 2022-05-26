# Imports
import hashlib
import os

users = {}  # Simple User Storage
print("PassHashManager successfully up and running")

# Add a user
print("Creating test account")
username = input("> Username: ")
password = input("> Password: ")

# Creating salt and key
salt = os.urandom(32)
key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
users[username] = {  # Storing salt and key
    'salt': salt,
    'key': key
}

# Verification
print("Test login")
username = input("> Check Username: ")
password = input("> Check Password: ")

if username in users:  # Check if username is found
    salt = users[username]['salt']  # Loading salt
    key = users[username]['key']  # Loading Key
    login_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)  # Creating login key

    # Cross-referencing login-key with stored username key
    if key == login_key:  # Login-key same as stored username key (Correct)
        print("Password was correct.")
    else:  # Login-key was not the same as stored username key (Incorrect)
        print("Password was incorrect.")
else:  # Username not found
    print("Username not found.")
