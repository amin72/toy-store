from django.utils.http import urlencode
from django.shortcuts import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from drone.models import DroneCategory
from drone import views
from drone.urls import app_name


class DroneCategoryTests(APITestCase):
    @staticmethod
    def full_url(view_name):
        return reverse(f'{app_name}:{view_name}')

    def post_drone_category(self, name):
        url = self.full_url(views.DroneCategoryList.name)
        data = {'name': name}
        response = self.client.post(url, data, format='json')
        return response
    
    def test_post_and_get_drone_category(self):
        """
        Ensure we can create a new DroneCategory and then retrieve it
        """
        new_drone_category_name = 'Hexacopter'
        response = self.post_drone_category(new_drone_category_name)
        print('PK {}'.format(DroneCategory.objects.get().pk))
        
        assert response.status_code == status.HTTP_201_CREATED
        assert DroneCategory.objects.count() == 1
        assert DroneCategory.objects.get().name == new_drone_category_name

    def test_post_existing_drone_category_name(self):
        """
        Ensure we cannot create a DroneCategory with an existing name
        """
        new_drone_category_name = 'Duplicated Copter'
        
        response1 = self.post_drone_category(new_drone_category_name)
        assert response1.status_code == status.HTTP_201_CREATED
        
        response2 = self.post_drone_category(new_drone_category_name)
        print(response2)
        assert response2.status_code == status.HTTP_400_BAD_REQUEST
