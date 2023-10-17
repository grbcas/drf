from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsUser(BasePermission):
    def has_permission(self, request, view):
        return request.user == view.get_object().user


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
