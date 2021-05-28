from django.test import TestCase
from django.utils import timezone

from apps.authentication.models import User


class TestSetUp(TestCase):

    def createUser(self):
        return User.objects.create(
            username='testadmin', email='email@email.com', is_verified=False, is_active=False,
            is_staff=False, created_at=timezone.now(), updated_at=timezone.now())

    def test_create_user_with_model(self):
        w = self.createUser()
        self.assertTrue(isinstance(w, User))
        self.assertEqual(w.__str__(), w.email)


