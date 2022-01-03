from django.shortcuts import render, get_object_or_404
from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response


class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()

    def list(self, request):
        serializer_class = UserSerializer(self.queryset, many=True)
        return Response(serializer_class.data, status=status.HTTP_200_OK)

    # def create(self, request):
    #     pass

    # def retrieve(self, request, pk=None):
    #     pass

    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass
