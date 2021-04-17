from rest_framework.permissions import IsAuthenticated
from utils.constants import USER_ROLE_PUBLISHER, USER_ROLE_AUTHOR


class PublisherPermission(IsAuthenticated):
    message = 'Вы не паблишер'

    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.role == USER_ROLE_PUBLISHER


class AuthorPermission(IsAuthenticated):
    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.role == USER_ROLE_AUTHOR


class SomePermission(IsAuthenticated):
    def has_permission(self, request, view, obj):
        return obj.is_active
