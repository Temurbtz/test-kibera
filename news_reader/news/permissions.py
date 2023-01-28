from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    message = 'You are not the owner of this new'

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False
    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False