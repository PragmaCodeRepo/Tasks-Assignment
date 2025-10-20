
from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth.models import AnonymousUser
from .models import Token

class TokenAuthForGraphQLMiddleware(MiddlewareMixin):
    """
    Authenticate GraphQL requests with 'Authorization: Token <key>'
    """
    def process_request(self, request):
        if getattr(request, "user", None) and request.user.is_authenticated:
            return
        auth = request.headers.get("Authorization", "")
        if auth.startswith("Token "):
            key = auth.split(" ", 1)[1].strip()
            try:
                token = Token.objects.select_related("user").get(key=key)
                request.user = token.user
            except Token.DoesNotExist:
                request.user = AnonymousUser()
