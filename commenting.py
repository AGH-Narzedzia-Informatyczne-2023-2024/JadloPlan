class User:
    def __init__(self, username):
        self.username = username
        self.posts = []

class Post:
    def __init__(self, author, content):
        self.author = author
        self.content = content
        self.comments = []
        self.ratings = []

    def add_comment(self, user, comment):
        self.comments.append((user, comment))

    def delete_comment(self, user, comment):
        if (user, comment) in self.comments:
            self.comments.remove((user, comment))
        else:
            print("Komentarz nie istnieje.")

    def add_rating(self, user, rating):
        if 1 <= rating <= 5:
            self.ratings.append((user, rating))
        else:
            print("Ocena powinna być w skali od 1 do 5.")

    def calculate_average_rating(self):
        if not self.ratings:
            return 0
        return sum(rating[1] for rating in self.ratings) / len(self.ratings)