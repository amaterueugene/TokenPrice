from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TokenSerializer
from prices.models import Token

class TokenAPIView(APIView):
     '''The only API view'''
     def get(self, request):
        token = Token.objects.all()
        return Response({'tokens': TokenSerializer(token, many=True).data})