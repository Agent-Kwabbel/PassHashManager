import hashlib
import os

users = {}  # Simple User Storage
print("PassHashManager successfully up and running")

# Creating an account
print("Creating account")
username = input("> Username: ")  # New account username input
password = input("> Password: ")  # New account password input

# Creating salt and a key
salt = os.urandom(32)
key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
users[username] = {  # Storing salt and key
    'salt': salt,
    'key': key
}

# Login
print("Test login")
username = input("> Check Username: ")  # Login username input
password = input("> Check Password: ")  # Login password input

# Check if username is found
if username in users:  # Username found
    salt = users[username]['salt']  # Loading salt of username
    key = users[username]['key']  # Loading key of username
    login_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)  # Creating login key

    # Cross-referencing login-key with stored key
    if key == login_key:  # Login-key same as stored username key (Correct)
        print("Password was correct.")
    else:  # Login-key was not the same as stored username key (Incorrect)
        print("Password was incorrect.")

else:  # Username not found
    print("Username not found.")
