from storage import load_users, save_users

def hash_password(password: str) -> int:
    return hash(password)

def create_user(username: str, password: str):
    users = load_users()

    if username in users:
        print ("Användarnamnet finns redan.")
        return False
    
    hashed_pw = hash_password(password)
    users[username] = {"password": hashed_pw}

    save_users(users)
    print (f"Användare '{username}' skapad!")
    return True

def login(username: str, password: str):
    users = load_users()

    if username not in users:
        print ("Användaren finns inte.")
        return False
    
    hashed_pw = hash_password(password)
    if users[username]["password"] == hashed_pw:
        print (f"Inloggad som {username}")
        return True
    else:
        print ("Fel lösenord")
        return False