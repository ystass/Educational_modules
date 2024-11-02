from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from modules.models import Lesson, Module
from modules.validators import UrlValidator


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [UrlValidator(field="url")]


class ModuleSerializer(ModelSerializer):
    lessons_count = SerializerMethodField()
    lessons = LessonSerializer(source="lesson_set", many=True, read_only=True)

    class Meta:
        model = Module
        fields = "__all__"

    def get_lessons_count(self, instance):
        return instance.lesson_set.count()
