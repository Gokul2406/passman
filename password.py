def get_password_input():
    domain_name = input("What is the name of the site or domain: ")
    password = input(f"What is the password for {domain_name}: ")
    print("Password added successfully") 
if __name__ == "__main__":
    get_password_input()
