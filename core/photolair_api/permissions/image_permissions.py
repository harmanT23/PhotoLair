from rest_framework.permissions import BasePermission


class IsAuthenticatedAndImageOwner(BasePermission):
    '''
    An authenticated user can only view or edit their own image
    '''

    def has_permission(self, request, view):
        """
        Only authenticated users have permission to view a specific image
        """
        if request.user and request.user.is_authenticated:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        """
        Only the authenticated user can edit their own image.
        """
        return request.user.id == obj.user.id
        