from rest_framework.serializers import ModelSerializer

from modules.models import Lesson, Module
from modules.validators import UrlValidator


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [UrlValidator(field="url")]


class ModuleSerializer(ModelSerializer):

    class Meta:
        model = Module
        fields = "__all__"
