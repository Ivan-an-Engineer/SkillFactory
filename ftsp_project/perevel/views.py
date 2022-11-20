from rest_framework.response import Response

from rest_framework.views import APIView
from .serializers import PerevalSerializer, UserSerializer, CoordsSerializer, ImageSerializer


class PerevalCreateView(APIView):
    def post(self, request):
        user = UserSerializer(data=request.data.get('user'))
        if user.is_valid():
            user.save()
        serializer = PerevalSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=201)



