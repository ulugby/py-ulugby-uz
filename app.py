from webob import Request, Response

class PyUlugbyApp:
    def __call__(self, environ, start_response):
        request = Request(environ)

        response = self.hande_request(request)

        return response(environ, start_response)
    
    def hande_request(self, request):
        user_agent = request.environ.get("HTTP_USER_AGENT", "User Agent Not Found")
        response = Response()
        response.text = f"Hello my friend with user agent {user_agent}"

        return response