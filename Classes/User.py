from Classes import trivia_game


class User:
    def __init__(self, username, discriminator, points=0, questions_correct=0, questions_answered=0, begin_date="", end_date=""):
        self.full_name = f"{username}#{discriminator}"
        db = trivia_game.get_trivia_db()
        _user = db.get_user(self.full_name)
        if _user is None:
            self.end_date = end_date
            self.begin_date = begin_date
            self.questions_correct = questions_correct
            self.points = points
            self.username = username
            self.discriminator = discriminator
            self.questions_answered = questions_answered
            db.insert_user(self)
        # else use what's in db
        else:
            self.username = _user[2]
            self.discriminator = _user[3]
            self.points = _user[4]
            self.questions_correct = _user[5]
            self.questions_answered = _user[6]
            self.begin_date = _user[7]
            self.end_date = _user[8]
