from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from modules.models import Lesson, Module
from modules.pagination import ModulesPaginator
from modules.serializer import LessonSerializer, ModuleSerializer
from users.permissions import IsTeacher, IsOwner


class ModuleViewSet(ModelViewSet):
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    pagination_class = ModulesPaginator

    def perform_create(self, serializer):
        module = serializer.save()
        module.owner = self.request.user
        module.save()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = (IsTeacher, )
        elif self.action in ['update', 'retrieve']:
            self.permission_classes = (IsTeacher | IsOwner, )
        elif self.action == 'destroy':
            self.permission_classes = (IsOwner, )
        return super().get_permissions()


class LessonCreateAPIView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsTeacher, IsAuthenticated]

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonListAPIView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    pagination_class = ModulesPaginator


class LessonRetrieveAPIView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsTeacher | IsOwner]


class LessonUpdateAPIView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsTeacher | IsOwner]


class LessonDestroyAPIView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwner]
