from django import views
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.utils.decorators import method_decorator

User = get_user_model()


@method_decorator(staff_member_required, name="dispatch")
class AuthorizationMatrixView(views.generic.base.TemplateView):

    template_name = "admin/authorization/authorization_matrix.html"

    def get(self, request):
        groups = Group.objects.prefetch_related("permissions").order_by("name")
        users = User.objects.prefetch_related("groups")
        permissions = Permission.objects.all().order_by(
            "content_type__app_label", "name"
        )

        user_group_matrix = [
            {"user": user, "groups": [group in user.groups.all() for group in groups]}
            for user in users
        ]

        group_permission_matrix = [
            {
                "permission": permission,
                "groups": [permission in group.permissions.all() for group in groups],
            }
            for permission in permissions
        ]

        context = {
            "groups": groups,
            "user_group_matrix": user_group_matrix,
            "group_permission_matrix": group_permission_matrix,
        }

        return self.render_to_response(context)
