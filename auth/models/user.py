from appconfig import db


class User(db.Model):
    ''' The data model'''
    # table name
    __tablename__ = 'users'
    userid = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    # short_url = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
   