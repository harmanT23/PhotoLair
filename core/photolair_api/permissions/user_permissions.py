from rest_framework.permissions import BasePermission


class IsAuthenticatedAndOwner(BasePermission):
    '''
    Permission Setting: An authenticated user can only view and edit their own 
    profile
    '''

    message = (
        'A user can only editing or view their own profile'
    )

    def has_permission(self, request, view):
        """
        Only authenticated users can access this endpoint
        """
        if request.user and request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        """
        Only the authenticated user can view/edit their own profile
        """
        return request.user.id == obj.id
        