class book:
    def __init__(self, ID, title, author):
        self.ID = ID
        self.title = title
        self.author = author

    def __str__(self) -> str:
        return f"ID: {self.ID}, Title: {self.title}, Author: {self.author}"