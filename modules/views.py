from rest_framework.viewsets import ModelViewSet

from modules.models import Module

from modules.pagination import ModulesPaginator
from modules.serializer import ModuleSerializer


class ModuleViewSet(ModelViewSet):
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    pagination_class = ModulesPaginator
