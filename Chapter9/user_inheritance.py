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
        
class Admin(User):
    base_user = ""
    privileges = ""
    
    def __init__(self, first_name, last_name, birthday, password_hash, security_level, identity_number, privileges):
        super().__init__(first_name, last_name, birthday, password_hash, security_level, identity_number)
        self.privileges = Privileges(privileges)
        self.base_user = User(first_name, last_name, birthday, password_hash, security_level, identity_number)
            
class Privileges:
    privileges = []
    
    def __init__(self, privileges):
        self.privileges = privileges
    
    def show_privileges(self):
        print(f"This user has the following privileges:")
        for priv in self.privileges:
            print(f"\t{priv}")
    
        
privileges = ["can post", "can edit self post", "can edit other posts", "can upload"]
first_user = Admin("John", "Doe", "01-09-98", "ea07f3687071fae7c435e58fe29df865", "3", "4039228329", privileges)

first_user.privileges.show_privileges()