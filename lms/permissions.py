from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):
    """
    Moderators access
    """
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Moderators').exists()


class IsOwnerOrModerator(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.groups.filter(name='Moderators').exists() or request.user == obj.user


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
