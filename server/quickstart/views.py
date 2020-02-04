from django.contrib.auth.models import Group, User
from rest_framework import viewsets

from .serializers import GroupSerializer, UserSerializer

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    Api endpoint that allows users to ve viewed or edited
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    Api endpoint that allos grous to be viewed or edited
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
