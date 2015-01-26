from app import db


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(254))
    website = db.Column(db.String(100))
    comment = db.Column(db.Text)
    date = db.Column(db.DateTime)

    def __init__(self, name, email, website, comment, date):
        self.name = name
        self.email = email
        self.website = website
        self.comment = comment
        self.date = date

    # It is def __str__ in Django.
    def __repr__(self):
        return self.comment
