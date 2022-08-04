from jwt import JWT

class UserResource:
    def getResource(self, user):
        del user['password']
        # accessToken = JWT().encode({'user': user}, "")
        accessToken = ""
        user_resource = {
            "accessToken": accessToken,
            "expiryAt": -1,
            "user": user
        }
        return user_resource