import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# 1 Option

random_people = random.choice(friends)

print(random_people)

# 2nd Option

random_index = random.randint(0, 4)

print(friends[random_index])