from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission

from import_export import fields, resources
from import_export.admin import ExportMixin

# USERS

User = get_user_model()

username_attribute = getattr(User, "USERNAME_FIELD", "username")
email_attribute = getattr(User, "EMAIL_FIELD", "email")


class UserGroupResource(resources.ModelResource):
    username = fields.Field(attribute=username_attribute, column_name="Username")
    email = fields.Field(attribute=email_attribute, column_name="E-mail")
    last_login = fields.Field(attribute="last_login", column_name="Laatst gewijzigd")
    is_active = fields.Field(attribute="is_active", column_name="Actief")
    is_staff = fields.Field(attribute="is_staff", column_name="Admin toegang")
    is_superuser = fields.Field(
        attribute="is_superuser", column_name="Admin supergebruiker"
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "last_login",
            "is_active",
            "is_staff",
            "is_superuser",
        )
        export_order = fields

    def dehydrate(self, user):
        data = super().dehydrate(user)
        group_names = [group.name for group in Group.objects.all()]
        for group_name in group_names:
            data[group_name] = group_name in [group.name for group in user.groups.all()]
        return data

    def export(self, queryset, *args, **kwargs):
        queryset = self.get_queryset()
        dataset = super().export(queryset, *args, **kwargs)
        group_names = [group.name for group in Group.objects.all()]
        for group_name in group_names:
            dataset.append_col(
                [
                    user.groups.filter(name=group_name).exists()
                    for user in User.objects.all()
                ],
                header=group_name,
            )
        return dataset

    def get_queryset(self):
        return super().get_queryset()


# GROUPS


class GroupPermissionResource(resources.ModelResource):
    name = fields.Field(attribute="name", column_name="Groep")

    class Meta:
        model = Group
        fields = ("name",)
        export_order = fields

    def dehydrate(self, group):
        data = super().dehydrate(group)
        permission_names = [permission.name for permission in Permission.objects.all()]
        for permission_name in permission_names:
            data[permission_name] = permission_name in [
                permission.name for permission in group.permissions.all()
            ]
        return data

    def export(self, queryset, *args, **kwargs):
        dataset = super().export(queryset, *args, **kwargs)
        permission_names = [permission.name for permission in Permission.objects.all()]
        for permission_name in permission_names:
            dataset.append_col(
                [
                    group.permissions.filter(name=permission_name).exists()
                    for group in queryset
                ],
                header=permission_name,
            )
        # Transpose the dataset
        dataset = dataset.transpose()
        # Rename the first column to "Groep"
        dataset.headers[0] = "Groep"
        return dataset


class CustomGroupAdmin(ExportMixin, admin.ModelAdmin):
    resource_classes = (UserGroupResource, GroupPermissionResource)
    search_fields = ("name",)
    ordering = ("name",)
    filter_horizontal = ("permissions",)
    change_list_template = "admin/auth/group/change_list.html"

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name == "permissions":
            qs = kwargs.get("queryset", db_field.remote_field.model.objects)
            # Avoid a major performance hit resolving permission names which
            # triggers a content_type load:
            kwargs["queryset"] = qs.select_related("content_type")
        return super().formfield_for_manytomany(db_field, request=request, **kwargs)


admin.site.unregister(Group)
admin.site.register(Group, CustomGroupAdmin)
