from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from website.models import Service, Recording, User
from .serializers import ServiceSerializer, RecordsSerializer, UserSerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrIsAdmin, IsOwnerRecordOrIsAdmin


class UserRetrieveUpdateDelete(APIView):
    permission_classes = [IsOwnerOrIsAdmin]

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs.get('pk', None))
        serializer = UserSerializer(user)
        if request.user.is_staff:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs.get('pk', None))
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        question = get_object_or_404(User, pk=kwargs.get('pk', None))
        question.delete()
        return Response("User deleted", status=status.HTTP_204_NO_CONTENT)


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAdminOrReadOnly]


class RecordsViewSet(viewsets.ModelViewSet):
    queryset = Recording.objects.all()
    serializer_class = RecordsSerializer
    permission_classes = [IsOwnerRecordOrIsAdmin]
