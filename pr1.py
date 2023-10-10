class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class Buyer(User):
    def __init__(self, username, password, address, id):
        super(Buyer, self).__init__(username, password)
        self.address = address
        self.id = id


user = Buyer('zynb', '123', 'iran', 22)
print(user.username , '' , user.password , '' , user.address , '' , user.id)

