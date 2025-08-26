class User:
    def __init__(self, username: str):
        self.username = username

    def to_dict(self):
        return {"username": self.username}
