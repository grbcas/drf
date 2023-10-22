from rest_framework.test import APITestCase


class LmsTestCase(APITestCase):

    def setUp(self) -> None:
        pass

    def test_create_Lesson(self):
        """
        Test - create Lesson
        :return:
        """
        data = {
            'name': 'test',
            'description': 'test'
        }

        response = self.client.post(
            '/lessons/',
            data=data
        )

        