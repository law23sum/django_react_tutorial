import rest_framework.permissions
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import generics

from api.models import Snippet
from api.permissions import IsOwnerOrReadOnly
from api.serializers import SnippetSerializer, UserSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [rest_framework.permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [rest_framework.permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
