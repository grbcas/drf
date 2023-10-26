from django.contrib.auth.models import Group, Permission
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from lms.models import Course, Lesson, Subscription
from users.models import User


class LessonAPITestCase(APITestCase):
    def setUp(self):
        # self.url = '/lessons/'
        # Подготовка данных перед каждым тестом
        self.user = User.objects.create(
            email='test_user@user.user',
            password='user@user.user',
            is_active=True,
            is_staff=False,
            is_superuser=False,

        )

        self.course = Course.objects.create(
            name='test_course',
            user=self.user
        )

        self.lesson = Lesson.objects.create(
            name='test_lesson',
            course=self.course,
            user=self.user
        )

        self.client.force_authenticate(user=self.user)

    def test_get_lessons_list(self):
        """ get list from lms:lessons """

        response = self.client.get(reverse('lms:lessons_list'))

        self.assertEqual(response.status_code,
                         status.HTTP_200_OK
                         )

        self.assertEqual(response.json(),
                         {
                             "count": 1,
                             "next": None,
                             "previous": None,
                             "results": [
                                 {
                                     "id": 1,
                                     "name": "test_lesson",
                                     "description": None,
                                     "course": 1,
                                     "link_video": None
                                 }
                             ]
                         }
                         )

    def test_lesson_retrieve(self):

        response = self.client.get(
            reverse('lms:lesson_retrieve', kwargs={'pk': self.lesson.pk})
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
                    response.json(),
                    {
                        "id": self.lesson.pk,
                        "name": "test_lesson",
                        "description": None,
                        "course": self.course.pk,
                        "link_video": None
                    }
        )

    def test_lesson_create(self):

        data = {
            "name": "test_create",
            "link_video": "https://www.youtube.com/test_create",
            "course": self.course.pk
            }

        response = self.client.post(
            reverse('lms:lesson_create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            Lesson.objects.all().count(),
            2
        )

    def test_lesson_update(self):

        update_data = {
            'name': 'test_lesson_update',
        }

        response = self.client.patch(
            reverse('lms:lesson_update', kwargs={'pk': self.lesson.pk}),
            data=update_data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
                    response.json(),
                    {
                        'course': self.course.pk,
                        'description': None,
                        'id': self.lesson.pk,
                        'link_video': None,
                        "name": "test_lesson_update",
                    }
        )

    def test_lesson_delete(self):

        response = self.client.delete(
            reverse('lms:lesson_delete', kwargs={'pk': self.lesson.pk})
        )

    def test_is_subscribed(self):
        data = {
            "user": self.user.pk,
            "course": self.course.pk
            }

        response = self.client.post(
            reverse('lms:subscription_create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        subscription_state = Subscription.objects.filter(course=self.course, user=self.user).exists()

        self.assertEqual(subscription_state, True)
