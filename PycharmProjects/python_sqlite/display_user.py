from main import User

myUsers = User.select()
for user in myUsers:
    print(user.name, user.email, user.password)


