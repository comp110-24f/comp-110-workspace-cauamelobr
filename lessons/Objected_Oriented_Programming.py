class Profile:
    username: str  # declaring attributes
    bio: str
    followers: int
    following: int
    private: bool

    def __init__(self):  # pay attention to the two __
        self.username = "usr9"
        self.bio = ""
        self.followers = 0
        self.following = 0
        self.private = False


my_prof: Profile = Profile()  # Construct a new profile, input the attributes
my_prof.username = "comp110fan"  # acessing the username attribute
print(my_prof.private)
