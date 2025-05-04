import bcrypt
from sqlalchemy.orm import Session
from src.models.user_model import User
from src.schemas.user_schema import UserSchema
from src.utils.response import api_response

def create_user(db: Session, user: UserSchema):
    try:
        existed_user = db.query(User).filter(User.email == user.email).first()
        if existed_user:
            return api_response(400, "User already exist")
        else:
            # Hash the password
            hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
            user.password = hashed_password.decode('utf-8')
            db_user = User(email=user.email, password=user.password)
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
            return db_user
    except Exception as e:
        return api_response(500, "Failed to add user", str(e))
    


        
    
    
    
    
