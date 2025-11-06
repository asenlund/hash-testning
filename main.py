from user_manager import create_user, login

def main():
    while True:
        print("\n === MENY ===")
        print("1. Skapa användare")
        print("2. Logga in")
        print("3. Avsluta")
        choice = input("Välj ett alternativ: ")

        if choice == "1":
            username = input("Ange användarnamn: ")
            password = input("Ange lösenord: ")
            create_user(username, password)

        
        elif choice == "2":
            username = input("Ange användarnamn: ")
            password = input("Ange lösenord: ")
            login(username, password)
        
        elif choice == "3":
            print ("Hejdå!")
            break

if __name__ == "__main__":
    main()
