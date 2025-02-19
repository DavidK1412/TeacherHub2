from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView

class VerifyTokenView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]  

    def get(self, request):
        user = request.user 

        if user.is_authenticated:
            return Response({
                'id': user.id,
                'role': user.role,  
            }, status=status.HTTP_200_OK)
        
        return Response({
            'detail': 'Token invalid or expired'
        }, status=status.HTTP_401_UNAUTHORIZED)
