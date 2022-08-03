import jwt

class UserResource:
    def getResource(self, user):
        del user['password']
        accessToken = jwt.encode({'user': user}, 'P80y97z9K4', algorithm='HS256')
        user_resource = {
            "accessToken": accessToken,
            "expiryAt": -1,
            "user": user
        }
        return user_resource