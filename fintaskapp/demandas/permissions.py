from rest_framework.permissions import BasePermission


class UserIsOwnerDemanda(BasePermission):

    def has_object_permission(self, request, view, demanda):
        return request.user.id == demanda.anunciante.id
