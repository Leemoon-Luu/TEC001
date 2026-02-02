correct_username= "python"
correct_password= "rules"

def login():
    i= 0

    while i< 5:
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        if username == correct_username and password == correct_password:
            print("Welcome!")
            return
        else:
            i += 1
    print("Access denied.")

login()