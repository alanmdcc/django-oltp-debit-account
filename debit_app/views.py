from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer


@api_view(['GET'])
def endpoints(_):
    data = ['/user']
    return Response(data)

class UserView(APIView):

    def get(self, _):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = User.objects.create(
            age=request.data['age'],
            name=request.data['name']
        )
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)

class UserDetailView(APIView):

    def get_user(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            raise Http404

    def get(self,request,id):
        user = self.get_user(id=id)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)

    def put(self,request,id):
        user = self.get_user(id=id)
        user.age = request.data['age']
        user.name = request.data['name']
        user.save()
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)

    def delete(self,request,id):
        user = self.get_user(id=id)
        user.delete()
        return Response('User was deleted')