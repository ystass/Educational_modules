from rest_framework.serializers import ModelSerializer

from modules.models import Module


class ModuleSerializer(ModelSerializer):

    class Meta:
        model = Module
        fields = "__all__"