from django.test import TransactionTestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import User


class UserTestCase(TransactionTestCase):
    def setUp(self):
        self.client = APIClient()
        User.objects.all().delete()

    def test_get_user(self):
        User.objects.create(age=20, name="Alan")
        User.objects.create(age=30, name="Carlos")

        response = self.client.get('/api/user/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        users = response.json()
        self.assertEqual(len(users), 2)

    def test_post_user(self):
        user = {'age': 20, 'name': 'Adam'}

        response = self.client.post('/api/user/', user)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        item = response.json()
        self.assertEqual(item['name'], 'Adam')

        self.assertEqual(User.objects.count(), 1)

    def test_put_user(self):
        self.userToUpdate = User.objects.create(age=20, name="Adam")
        new_data = {'age': 21, 'name': 'Adam'}

        response = self.client.put(f'/api/user/{self.userToUpdate.id}', new_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        updated_user = response.json()
        self.assertEqual(updated_user['age'], 21)

        self.assertEqual(User.objects.count(), 1)

        self.userToUpdate.refresh_from_db()
        self.assertEqual(self.userToUpdate.age, 21)

    def test_delete_user(self):
        self.userToDelete = User.objects.create(age=40, name="Sam")

        response = self.client.delete(f'/api/user/{self.userToDelete.id}')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertFalse(User.objects.filter(id=self.userToDelete.id).exists())
