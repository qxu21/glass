from app import db

"""
class User(db.Model): #currently unused
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.LargeBinary)
    email = db.Column(db.String(120), index=True, unique=True)
    players = db.relationship('Player', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % (self.username)

    #is the user allowed to authenticate?
    @property
    def is_authenticated(self):
        return True
    
    #is the user active and unbanned?
    @property
    def is_active(self):
        return True
    
    #for fake users that can't login
    @property
    def is_anonymous(self):
        return False
    
    #return an id
    def get_id(self):
        return str(self.id)
        """

#guess who gets to keep these manually updated between scribe and this, because scribe can't sqlalchemy?
#me, that's who
class Name(db.Model):
    __tablename__ = 'names' #hope this works
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(102))

class Guild(db.Model):
    __tablename__ = 'guilds'
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(102))
    pwd = db.Column(db.String(30))