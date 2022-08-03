class ErrorResource:
    def getResource(self, status, message):
        error_resource = {
            "status": status,
            "message": message
        }
        return error_resource