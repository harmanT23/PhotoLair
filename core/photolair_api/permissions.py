class IsUserOwnerOnly(BasePermission):
    '''
    An authenticated user can only view and edit their own profile
    '''

    message = (
      'Editing/Viewing a user\'s profile is restricted to the original user'
    )

    def has_permission(self, request, view):
        """
        Only authenticated users have permission to view a user profile
        """
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        """
        The authenticated user can only view their own profile
        """
        return request.user.id == obj.id