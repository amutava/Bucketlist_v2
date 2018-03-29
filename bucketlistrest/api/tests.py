# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


from .models import Bucketlist

# Create your tests here.


class ModelTestCase(TestCase):
    '''This class defines the test suite for the bucketlist model.'''

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        user = User.objects.create(username="angiem")
        self.client.force_authenticate(user=user)
        self.bucketlist_details = {
            'name': 'Visit cousins',
            'description': 'Canada',
            'owner': user.id}
        self.bucketlist_name = "Become a world class developer"
        self.bucketlist = Bucketlist(name=self.bucketlist_name, owner=user)
        self.response = self.client.post(
            reverse('create'),
            self.bucketlist_details,
            format="json")
        self.item = {
            'name': 'Visit Mongolia too'
        }

    def test_authorization_is_enforced(self):
        '''Test that the api has user authorization.'''
        new_client = APIClient()
        res = new_client.get('/bucketlists/', kwargs={'pk': 3}, format="json")
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_api_can_get_a_bucketlist(self):
        """Test the api can get a given bucketlist."""
        bucketlist = Bucketlist.objects.get(id=1)
        response = self.client.get(
            '/bucketlists/',
            kwargs={'pk': bucketlist.id}, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, bucketlist)

    def test_model_can_create_a_bucketlist(self):
        '''
            Test the bucketlist model can create a bucketlist.
        '''
        old_count = Bucketlist.objects.count()
        self.bucketlist.save()
        new_count = Bucketlist.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_api_can_create_a_bucketlist(self):
        '''
            Test the api has bucket creation capability.
        '''
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_update_bucketlist(self):
        '''
        Test the api can update a given bucketlist.
        '''
        bucketlist = Bucketlist.objects.get()
        change_bucketlist = {'name': 'Visit Japan'}
        response = self.client.put(
            reverse('details', kwargs={'pk': bucketlist.id}),
            change_bucketlist, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_delete_bucketlist(self):
        '''Test the api can delete a bucketlist.'''
        bucketlist = Bucketlist.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': bucketlist.id}),
            format='json',
            follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
