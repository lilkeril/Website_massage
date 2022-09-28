from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.views import APIView
from website.models import Service, Recording, User
from .serializers import ServiceSerializer, RecordsSerializer, UserSerializer
from .permissions import IsAdminOrReadOnly
# class RecordsAPIView(APIView):
#
#     def get(self, request):
#         records = Recording.objects.all()
#         return Response({'records': RecordsSerializer(records, many=True).data})
#
#     def post(self, request):
#         serializer = RecordsSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'record': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Method PUT not allowed'})
#
#         try:
#             instance = Recording.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Object does not exists'})
#
#         serializer = RecordsSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'record': serializer.data})


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (IsAdminOrReadOnly, )


class RecordsViewSet(viewsets.ModelViewSet):
    queryset = Recording.objects.all()
    serializer_class = RecordsSerializer
    permission_classes = (IsAdminUser, )

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

    def get_queryset(self):
        owner_queryset = self.queryset.filter(customer=self.request.user)
        return owner_queryset
