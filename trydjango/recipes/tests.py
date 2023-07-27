from django.contrib.auth import get_user_model
from django.test import TestCase



User = get_user_model()

class UserTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('mom', password='password')
    
    def test_check_password(self):
        checked = self.user_a.check_password('password')
        return self.assertTrue(checked)