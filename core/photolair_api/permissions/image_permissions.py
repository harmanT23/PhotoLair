from rest_framework.permissions import BasePermission


class IsAuthenticatedAndImageOwner(BasePermission):
    '''
    Permission Setting: An authenticated user can only edit their own 
    image.
    '''

    message = (
        'Editing/Viewing a image is restricted to the author of the image'
    )

    def has_permission(self, request, view):
        """
        Only authenticated users can access this endpoint.
        """
        if request.user and request.user.is_authenticated:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        """
        Only the authenticated user can edit/delete their own image.
        """
        return request.user.id == obj.user.id
        