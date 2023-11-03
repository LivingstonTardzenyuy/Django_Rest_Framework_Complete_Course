from rest_framework import permissions

class IsAdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:          #get method. 
            return True 
        else:
            return bool(request.user and request.user.is_staff)

class IsReviewUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:          #check if the request is a get method
            return True 
        
        else:
            return obj.review_user == request.user or request.user.is_staff     #allow only users that publish thier review to have access to update/edit


