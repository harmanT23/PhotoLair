from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response


class BlackListTokenView(APIView):
    """
    Blacklist Token Endpoint
    - POST: Blacklist the user's refresh token 
    """
    permission_classes = [AllowAny,]

    def post(self, request):
        """
        Blacklist the given refresh token.
        """
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
