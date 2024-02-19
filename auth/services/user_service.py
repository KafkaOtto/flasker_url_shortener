from models.user import User
from appconfig import db
from .self_md5 import md5

def password_hash(pswd:str) -> str:
    # please implement hash here...
    return md5.md5(pswd)

def create_new_user(body):
    username = body['username']
    password = password_hash(body['password'])
    
    # if username is None or password is None:
    #     raise Exception("Incomplete/invalid input")
    
    existing_user = User.query.filter_by(username = username).first()
    if existing_user:
        return None
    
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    return new_user.as_dict()

def get_all_users():
    users = User.query.all()
    users = [user.as_dict() for user in users]
    return users

def reset_passwords(body):
    username = body['username']
    old_password = password_hash(body['old-password'])
    new_password = password_hash(body['new-password'])

    user = User.query.filter_by(username=username).first()
    if user is None:
        raise Exception("User doesn't exist")
    
    if user.password != old_password:
        return False
    else:
        user.password = new_password
        db.session.commit()
        return True
        
def user_login(body):
    username = body['username']
    password = password_hash(body['password'])
    
    user = User.query.filter_by(username=username).first()
    if user.password != password:
        return None
    return user.as_dict()

    
    