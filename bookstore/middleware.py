from django.db import connection

class CloseDBConnectionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        connection.close()  # Close the connection after the response is sent
        return response
