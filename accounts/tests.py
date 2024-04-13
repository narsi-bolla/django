from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='nara', email='nara@email.com', password='123'
        )

        self.assertEquals(user.username, "nara")
        self.assertEquals(user.email, "nara@email.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)


    def create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="root", email="root@email.com", password="123"
        )

        self.assertEquals(admin_user.username, "root")
        self.assertEquals(admin_user.email, "root@email.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)