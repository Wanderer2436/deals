import io
import os

from django.conf import settings
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class TestBase(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()


class TestCustomerAPIView(TestBase):
    def test_list_data(self) -> None:
        url = 'core:customers'
        response = self.client.get(reverse(url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestDealFileUploadAPIView(TestBase):
    def test_read_file(self) -> None:
        file_path = os.path.join(settings.BASE_DIR, 'core/tests/deals_test.csv')
        file = io.open(file_path, 'rb', buffering=0)
        url = 'core:deals_file'
        data = {
            'deals': file
        }
        response = self.client.post(reverse(url), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

