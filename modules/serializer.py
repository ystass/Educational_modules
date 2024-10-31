from rest_framework.serializers import ModelSerializer

from modules.models import Lesson, Module


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class ModuleSerializer(ModelSerializer):

    class Meta:
        model = Module
        fields = "__all__"
