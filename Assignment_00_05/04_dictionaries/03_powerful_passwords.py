#This can be done via something called hashing. Hashing is when we take something and convert it into a different, unique identifier. This is done using a hash function. Luckily, there are several resources that can help us with this.
#For example, using a hash function called SHA256(...) something as simple ashellocan be hashed into a much more complex2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
#Fill out the login(...) function for a website that hashes their passwords. Login should return True if an email's stored password hash in stored_logins is the same as the hash of password_to_check.(Hint. You will need to use the provided hash_password(...) function. You don't necessarily need to know how it works, just know that hash_password(...) returns the hash for the password!)

from hashlib import sha256

# Function to check if login is successful
def login(email, stored_logins, password_to_check):
    """
    Checks if the given email exists and if the hashed password matches.

    email: User's email as a string.
    stored_logins: A dictionary where keys are emails and values are hashed passwords.
    password_to_check: The plain-text password to verify.
    
    Returns True if the email exists and password matches, otherwise False.
    """
    # Check if the email exists in stored_logins
    if email not in stored_logins:
        print(f"Login failed: Email '{email}' not found.")
        return False

    # Compare stored hashed password with the hash of the entered password
    if stored_logins[email] == hash_password(password_to_check):
        print(f"Login successful for {email} ✅")
        return True
    else:
        print(f"Login failed: Incorrect password for {email} ❌")
        return False

# Function to hash a password using SHA256
def hash_password(password):
    """
    Hashes the input password using SHA256.

    password: A string containing the password to hash.

    Returns the hexadecimal representation of the hash.
    """
    return sha256(password.encode()).hexdigest()

# Main function to test login functionality
def main():
    # Dictionary of stored emails and their hashed passwords
    stored_logins = {
        "user@example.com": hash_password("mypassword123"),
        "admin@secure.com": hash_password("AdminPass#789"),
        "hello@website.com": hash_password("securepass"),
    }

    # Test cases
    print("\n🔹 Running Login Tests 🔹\n")
    
    # Correct passwords
    login("user@example.com", stored_logins, "mypassword123")
    login("admin@secure.com", stored_logins, "AdminPass#789")
    
    # Incorrect passwords
    login("user@example.com", stored_logins, "wrongpassword")
    login("admin@secure.com", stored_logins, "adminpass#789")  # Case-sensitive test
    
    # Email not found
    login("unknown@domain.com", stored_logins, "password")

if __name__ == "__main__":
    main()