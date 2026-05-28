class User:

    # This is a variable (parameter attach to an object)(what the object has)
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    # This is a method (a function that attached to an object)
    def follow(self, user):
        user.followers += 1
        self.following += 1



user1 = User("001", "Dinda")
user2 = User("002", "Jefry")

user1.follow(user2)
print(user1.following)



