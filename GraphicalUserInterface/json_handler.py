import json
import hashlib

USERS_FILE = "./GraphicalUserInterface/users.json"

def readUsers():
    try:
        with open(USERS_FILE, "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        users = []
    
    return users

def writeUsers(users):
    with open(USERS_FILE, "w") as file:
        json.dump(users, file, indent=4)

def encryptPassword(password):
    # Encrypt the password using hashlib (e.g., SHA-256)
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def writeEventData(data):
    with open("event_data.json", "a") as file:
        json.dump(data, file)
        file.write("\n")
