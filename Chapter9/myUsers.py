from privileges import Privileges
from user import User
from admin import Admin

privileges = ["can post", "can edit self post", "can edit other posts", "can upload"]
first_user = Admin("John", "Doe", "01-09-98", "ea07f3687071fae7c435e58fe29df865", "3", "4039228329", privileges)

first_user.privileges.show_privileges()