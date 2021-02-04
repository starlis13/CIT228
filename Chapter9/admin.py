from privileges import Privileges
from user import User

class Admin(User):
    base_user = ""
    privileges = ""
    
    def __init__(self, first_name, last_name, birthday, password_hash, security_level, identity_number, privileges):
        super().__init__(first_name, last_name, birthday, password_hash, security_level, identity_number)
        self.privileges = Privileges(privileges)
        self.base_user = User(first_name, last_name, birthday, password_hash, security_level, identity_number)
