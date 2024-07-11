from django.urls import path

from .admin_views import AuthorizationMatrixView

urlpatterns = [
    path(
        "matrix",
        AuthorizationMatrixView.as_view(),
        name="authorization_matrix",
    ),
]
