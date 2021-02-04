class User:
    first_name = ""
    last_name = ""
    birthday = ""
    password_hash = ""
    security_level = ""
    identity_number = ""
    login_attempts = 0
    

    def __init__(self, first_name, last_name, birthday, password_hash, security_level, identity_number):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.password_hash = password_hash
        self.security_level = security_level
        self.identity_number = identity_number
    
    def describe_user(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Birthday: {self.birthday}")
        print(f"Password hash: {self.password_hash}")
        print(f"Security Level: {self.security_level}")
        print(f"ID: {self.identity_number}")
        
    def greet_user(self):
        print(f"Welcome, {self.first_name} {self.last_name}! I hope you are well!")
        
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0