from rest_framework import permissions

class IsStaffEditorPermission(permissions.DjangoModelPermissions):

    perms_map = {
        'GET': ['%(app_label)s.add_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    #give this one when you want to ensure that one or more specific user dont have perm
    # def has_permission(self, request, view):
    #     if not request.user.is_staff:
    #         return False
    #     return super().has_permission(request, view)



    #no need for this portion
    # def has_permission(self, request, view):
    #     user = request.user
    #     if user.is_staff:
    #         if user.has_perm("products.view_products"): #appname.verb_modelname
    #             return True
    #         if user.has_perm("products.change_products"):
    #             return True
    #         if user.has_perm("products.delete_products"):
    #             return True
    #         if user.has_perm("products.add_products"):
    #             return True
    #         return False
    #     return False