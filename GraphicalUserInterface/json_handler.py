import json
import hashlib

USERS_FILE = "./GraphicalUserInterface/users.json"

def read_users():
    try:
        with open(USERS_FILE, "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        users = []
    
    return users

def write_users(users):
    with open(USERS_FILE, "w") as file:
        json.dump(users, file, indent=4)

def encrypt_password(password):
    # Encrypt the password using hashlib (e.g., SHA-256)
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def write_event_data(data):
    with open("event_data.json", "a") as file:
        json.dump(data, file)
        file.write("\n")
