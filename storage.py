import json
import os

FILE_PATH = "users.json"

def load_users():
    if not os.path.exists(FILE_PATH):
        return{}
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:  # Tom fil
                return {}
            return json.loads(content)
    except json.JSONDecodeError:
        print("users.json är inte giltig JSON. Återställer filen.")
        return {}
    

def save_users(users):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4, ensure_ascii=False)