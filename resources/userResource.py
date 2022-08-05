import python_jwt as jwt, datetime
from jwt_key import jwt_key

class UserResource:
    def getResource(self, user):
        del user['password']
        accessToken = jwt.generate_jwt(user, jwt_key, 'PS256', datetime.timedelta(minutes=20160))
        user_resource = {
            "accessToken": accessToken,
            "user": user
        }
        return user_resource
  