from django.urls import path
from rest_framework.routers import SimpleRouter

from modules.apps import ModulesConfig
from modules.views import (LessonCreateAPIView, LessonDestroyAPIView,
                           LessonListAPIView, LessonRetrieveAPIView,
                           LessonUpdateAPIView, ModuleViewSet)

app_name = ModulesConfig.name

router = SimpleRouter()
router.register("", ModuleViewSet, basename="modules")

urlpatterns = [
    path("lessons/", LessonListAPIView.as_view(), name="lessons-list"),
    path("lessons/create/", LessonCreateAPIView.as_view(), name="create-lesson"),
    path("lessons/<int:pk>/", LessonRetrieveAPIView.as_view(), name="retrieve-lesson"),
    path(
        "lessons/<int:pk>/update/", LessonUpdateAPIView.as_view(), name="update-lesson"
    ),
    path(
        "lessons/<int:pk>/delete/", LessonDestroyAPIView.as_view(), name="delete-lesson"
    ),
]

urlpatterns += router.urls
