from django.contrib.auth import get_user_model
from django.test import RequestFactory, TestCase
from django.urls import reverse

from auth_matrix.admin_views import AuthorizationMatrixView

User = get_user_model()


class AuthorizationMatrixViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.view = AuthorizationMatrixView.as_view()
        self.admin_user = User.objects.create_user(
            username="test", password="test", is_staff=True, is_superuser=True
        )
        self.url = reverse("authorization_matrix")

    def test_view_requires_admin_permission(self):
        request = self.factory.get(self.url)
        request.user = User.objects.create_user(
            username="test_user",
            password="test_pass",
            is_staff=False,
            is_superuser=False,
        )

        response = self.view(request)

        self.assertEqual(response.status_code, 302)

    def test_view_returns_200_for_admin_user(self):
        request = self.factory.get(self.url)
        request.user = self.admin_user

        response = self.view(request)

        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        request = self.factory.get(self.url)
        request.user = self.admin_user

        response = self.view(request)

        self.assertEqual(
            response.template_name, ["admin/authorization/authorization_matrix.html"]
        )

    def test_view_context_contains_groups(self):
        request = self.factory.get(self.url)
        request.user = self.admin_user

        response = self.view(request)

        self.assertIn("groups", response.context_data)

    def test_view_context_contains_user_group_matrix(self):
        request = self.factory.get(self.url)
        request.user = self.admin_user

        response = self.view(request)

        self.assertIn("user_group_matrix", response.context_data)
        self.assertIsInstance(response.context_data["user_group_matrix"], list)

    def test_view_context_contains_group_permission_matrix(self):
        request = self.factory.get(self.url)
        request.user = self.admin_user

        response = self.view(request)

        self.assertIn("group_permission_matrix", response.context_data)
        self.assertIsInstance(response.context_data["group_permission_matrix"], list)
