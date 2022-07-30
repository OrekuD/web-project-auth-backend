class OkayResource:
    def getResource(self, message):
        okay_resource = {
            "status": 200,
            "message": message
        }
        return okay_resource