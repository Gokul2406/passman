from cryptography.fernet import Fernet

def get_password_input():
    print("Generating key")
    key = Fernet.generate_key()
    f = Fernet(key)
    domain_name = input("What is the name of the site or domain: ")
    password = input(f"What is the password for {domain_name}: ")
    encrypted_password = f.encrypt(str.encode(password))
    print("Password added successfully")   

if __name__ == "__main__":
    get_password_input()
