import jwt
from Models.user import User
from datetime import datetime, timedelta

class JwtService():
    
    SECRET = 'secret'
    ALGOS = 'HS256'

    def create(self, user):
        dt = datetime.now() + timedelta(days=1)
        encoded_jwt = jwt.encode({'user_id' : user.getId(), 'exp' : dt}, JwtService.SECRET, algorithm = JwtService.ALGOS)
        return encoded_jwt

    def verify(self, token):
        decoded_jwt = {}
        
        try :
            decoded_jwt = jwt.decode(token, JwtService.SECRET, algorithm = JwtService.ALGOS)
        except jwt.ExpiredSignatureError :
            print("pas à jour")
            return False
        except jwt.InvalidTokenError :
            print("Mauvais token")
            return False
        return True