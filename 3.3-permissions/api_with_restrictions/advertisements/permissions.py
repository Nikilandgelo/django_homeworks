from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    
    def has_object_permission(self, request, view, obj) -> True | False:
        return request.user == obj.creator or request.user.is_superuser