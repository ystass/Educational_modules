from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from modules.models import Module, Lesson
from users.models import User


class ModuleTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='admin@admin.com')
        self.module = Module.objects.create(serial_number='1', title='Биология')
        self.client.force_authenticate(user=self.user)

    def test_module_retrieve(self):
        url = reverse('modules:modules-detail', args=(self.module.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('title'), self.module.title
        )

    def test_module_create(self):
        url = reverse('modules:modules-list')
        data = {
           'serial_number': '2',
            'title': 'История',
            'description': 'Уроки по истории',
            'owner': self.user.pk
        }
        response = self.client.post(url, data)

        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Module.objects.all().count(), 2
        )

    def test_module_update(self):
        url = reverse('modules:modules-detail', args=(self.module.pk,))
        data = {'title': 'Физика'}
        response = self.client.patch(url, data)
        data = response.json()

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('title'), 'Физика'
        )

    def test_module_delete(self):
        url = reverse('modules:modules-detail', args=(self.module.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Module.objects.all().count(), 0
        )

    def test_module_list(self):
        url = reverse('modules:modules-list')
        response = self.client.get(url)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )


class LessonTestCase(APITestCase):

    def setUp(self):
        # Подготовка данных перед каждым тестом
        self.user = User.objects.create(email='admin@admin.com')
        self.module = Module.objects.create(serial_number='1', title='Алгебра', description='Уроки по Алгебре', owner=self.user)
        self.lesson = Lesson.objects.create(title='Введение', description='Начало', module=self.module, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse('modules:retrieve-lesson', args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('title'), self.lesson.title
        )

    def test_lesson_create(self):
        url = reverse('modules:create-lesson')
        data = {
            'title': 'Уравнения',
            'description': 'Примеры',
            'module': self.module.pk
        }
        response = self.client.post(url, data)

        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Lesson.objects.all().count(), 2
        )

    def test_lesson_update(self):
        url = reverse('modules:update-lesson', args=(self.lesson.pk,))
        data = {'title': 'Функции'}
        response = self.client.patch(url, data)

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            response.data.get('title'), 'Функции'
        )

    def test_lesson_delete(self):
        url = reverse('modules:delete-lesson', args=(self.lesson.pk,))
        response = self.client.delete(url)

        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Lesson.objects.all().count(), 0
        )

    def test_lesson_list(self):
        url = reverse('modules:lessons-list')
        response = self.client.get(url)

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            response.data,
            {'count': 1, 'next': None, 'previous': None, 'results':
                [{'id': self.lesson.pk, 'title': self.lesson.title, 'description': self.lesson.description,
                  'preview': None, 'url': None,
                  'module': self.lesson.module.pk, 'owner': self.lesson.owner.pk}]}
        )
