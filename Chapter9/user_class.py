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
        
    #9-5
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        

first_user = User("John", "Doe", "01-09-98", "ea07f3687071fae7c435e58fe29df865", "3", "4039228329")
second_user = User("Celeste", "Ludenburg", "04-16-89", "a4cffa0e0eebf835221fd2a3e530d85e", "5", "3948160169")
third_user = User("Bri", "O'Landry", "09-28-76", "d42e57d7a327593d9921fb33849629c7", "2", "0402491932")

#9-5
fourth_user = User("Youdont", "Wannano", "12-12-12", "70d428e1b1b6ce65fcd95dfdabd33de4", "4", "4815162342")

first_user.describe_user()
first_user.greet_user()

second_user.describe_user()
second_user.greet_user()

third_user.describe_user()
third_user.greet_user()

#9-5
while fourth_user.login_attempts < 30:
    fourth_user.increment_login_attempts()
    print(f"This moron has tried to login {fourth_user.login_attempts} times")

fourth_user.reset_login_attempts()
print(f"Alright, mercy. I've reset the user's login attempts to {fourth_user.login_attempts}")