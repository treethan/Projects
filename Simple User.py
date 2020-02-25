class User:
    """Builds a simple profile of a user"""
    def __init__(self, first_name, last_name, eye_color, job_title):
        """Initializes attributes for a user"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.eye_color = eye_color
        self.job_title = job_title.title()
        self.login_attempts = 0
   
    def describe_user(self):
        """Summary of user details"""
        print(f"{self.first_name} {self.last_name} is a {self.job_title} that has {self.eye_color} colored eyes.")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}! So very nice to meet you.")

    def increment_login_attempts(self):
        """Increments number of login attempts by 1"""
        self.login_attempts += 1
        print(f"Login attempts: {self.login_attempts}")
   
    def reset_login_attempts(self):
        """Sets login attempts to 0"""
        self.login_attempts = 0

class Admin(User):
    """child class of User"""
    def __init__(self, first_name, last_name, eye_color, job_title):
        """Initializes parent and child variables"""
        super().__init__(first_name, last_name, eye_color, job_title)

        self.privileges = Privileges()
   
class Privileges(Admin):
    """Class for user privileges"""
    def __init__(self, privileges=[]):
       """initializes child class attributes"""
       self.privileges = privileges

    def show_privileges(self):
        """shows the privileges of the user"""
        # self.privileges = ['can add post', 'can delete post', 'can ban user']
        print(f"The following user privileges for are: ")
        if self.privileges:
            for items in self.privileges:
                print(f"- {items}")
        else:
            print("- This user has no privileges.")

#creates user with indicated parameters
user1 = User("ethan", "berman", "blue", "it support technician")
#call describe method
user1.describe_user()
#call greet method
user1.greet_user()
#increment login attempts x3
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
#reset the login attempts
user1.reset_login_attempts()
#incremented again
user1.increment_login_attempts()
#second user created based on given parameters
user2 = User("kat", "tharp", "hazel", "administration assistant")
user2.describe_user()
user2.greet_user()
#third user created based on given parameters
user3 = User("emily", "berman", "blue", "certified nursing assistant")
user3.describe_user()
user3.greet_user()
#admin user created
user3 = Admin("emily", "berman", "blue", "certified nursing assistant")
user3.greet_user()
user3.describe_user()
#displays priveleges of user3
user3.privileges.show_privileges()
print("- Adding privileges -")
#adds below privileges to user3
user3_privileges = ['can add post', 'can delete post', 'can ban user']
user3.privileges.privileges = user3_privileges
user3.privileges.show_privileges()