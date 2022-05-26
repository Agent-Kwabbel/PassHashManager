# PassHashManager [v1.0.0]

Very simple Python script (*app.py*) for hashing, storing and checking login/account creating information. It can be used for creating accounts and for logging into those accounts. The hashing system includes SHA256, an 32 bytes long salt and 100,000 iterations. (This can be changed.)

The main purpose of this file (*app.py*) is to base everything of it. This is not a ready to go system, but only a file with a hashing and storing system. You need to change how the information will get into and out of the system, how you're going to run it, and maybe change the storage system. So use this file only for making an account password hashing system.

In the file *app.py* is an example system. Every input is done in the terminal and stored in the same file. You can test the system by running the file. Please note that if you're going to use this system, you need to change the way of getting the information and maybe the way of storing the information. The system also has some example print messages.

> **If you're making a password system, please never EVER store a non-hashed password or user info anywhere! Never! That's kinda the point of this hashing code.**
