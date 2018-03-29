# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.models import User


from .permissions import IsOwner
from .serializers import BucketlistSerializer,\
    UserSerializer, BucketListItemsSerializer
from .models import Bucketlist, BucketListItems


class CreateView(generics.ListCreateAPIView):
    '''
        This class defines the create behavior of our rest api.
    '''
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    # permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        '''
        Save the post data when creating a new bucketlist.
        '''
        serializer.save(owner=self.request.user)


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    # permission_classes = (permissions.IsAuthenticated, IsOwner)


class UserView(generics.ListAPIView):
    '''View to list the user queryset.'''
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailsView(generics.RetrieveAPIView):
    '''View to retrieve a user instance.'''
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BucketListItemsView(generics.ListCreateAPIView):
    queryset = BucketListItems.objects.all()
    serializer_class = BucketListItemsSerializer
    # permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        '''
        Save the post data when creating a new bucketlist item.
        '''
        serializer.save()


class ItemsDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = BucketListItems.objects.all()
    serializer_class = BucketlistSerializer
    # permission_classes = (permissions.IsAuthenticated,)
