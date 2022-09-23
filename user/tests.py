from django.test import Client, TestCase
from django.contrib.auth.models import User

# Create your tests here.
class UserTestCase(TestCase):
    """test cases for user application"""

    def setUp(self):
        """setups database for test cases"""
        # create a test user
        User.objects.create(username="tester", password="Pa$$w0rd!")

    def test_login_page(self):
        """test login page status"""
        client = Client()
        response = client.get("/user/accounts/login/")
        self.assertEqual(response.status_code, 200)

    def test_register_page(self):
        """tests register page status"""
        client = Client()
        response = client.get("/user/accounts/register/")
        self.assertEqual(response.status_code, 200)

    def test_logout_view(self):
        """test logout view"""
        client = Client()
        response = client.get("/user/accounts/logout/")
        self.assertEqual(response.status_code, 302)
