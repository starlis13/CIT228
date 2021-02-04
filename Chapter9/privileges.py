class Privileges:
    privileges = []
    
    def __init__(self, privileges):
        self.privileges = privileges
    
    def show_privileges(self):
        print(f"This user has the following privileges:")
        for priv in self.privileges:
            print(f"\t{priv}")
