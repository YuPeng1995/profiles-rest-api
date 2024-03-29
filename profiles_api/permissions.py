from rest_framework import permissions

# return True/False
class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check if user is trying to edit their own profile"""
        
        # for GET
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # check permission
        return obj.id == request.user.id
        
        
