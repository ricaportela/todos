from rest_framework.permissions import BasePermission

class UsersGroupsPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        groups = user.groups.all().values_list("name", flat=True)

        if not groups:
            return False

        if not [x for x in ["admin"] if x in groups]:
            return False

        return True