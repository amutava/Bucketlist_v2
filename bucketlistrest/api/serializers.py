from rest_framework import serializers
from django.contrib.auth.models import User


from .models import Bucketlist, BucketListItems


class BucketlistSerializer(serializers.ModelSerializer):
    '''
        Serializer to map the Model instance into JSON format.
    '''
    items = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field='name')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        '''
            Meta class to map serializer's fields with the model fields.
        '''
        model = Bucketlist
        fields = ('id', 'name', 'owner', 'description',
                  'date_created', 'date_modified', 'done', 'items')
        read_only_fields = ('date_created', 'date_modified')


class UserSerializer(serializers.ModelSerializer):
    '''
        A user serializer to aid in authentication and authorization.
    '''

    bucketlists = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Bucketlist.objects.all())

    class Meta:
        '''
            Map this serializer to the default django user model.
        '''
        model = User
        fields = ('id', 'username', 'bucketlists')


class BucketListItemsSerializer(serializers.ModelSerializer):
    '''
        A bucketlist Item serializer
    '''
    bucketlist_id = serializers.SlugRelatedField(
        queryset=Bucketlist.objects.all(), slug_field='name')

    class Meta:
        model = BucketListItems
        fields = ('id', 'name', 'bucketlist_id', 'date_created',
                  'date_modified', 'done')
        read_only_fields = ('date_created', 'date_modified')
