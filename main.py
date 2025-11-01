from auth import load_users, save_users, find_user, get_hash, bytes_to_hex
from user import User
from user_registration import create_user

def main():
    users_file = "usersdb.json"
    users = load_users(users_file)

    while True:
        print("1-login, 2-register, 3-exit:")
        choice = input()

        if choice == "3":
            save_users(users, users_file)
            break

        if choice == "2":
            username = input("Enter username: ")
            if find_user(users, username) is not None:
                print("Username already exists")
            else:
                password = input("Enter password: ")
                users.append(create_user(username, password))
                print("Registration is successful")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")

            user_from_db = find_user(users, username)
            if user_from_db is None:
                print("Username or password is incorrect")
            else:
                salt = user_from_db.salt
                new_hashed_pass = get_hash(password + salt)
                if user_from_db.hpass == new_hashed_pass:
                    print("Login is correct")
                else:
                    print("Username or password is incorrect")

if __name__ == "__main__":
    main()
