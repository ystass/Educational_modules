from django.contrib import admin

from modules.models import Module, Lesson


@admin.register(Module)
class UserCourse(admin.ModelAdmin):
    list_display = ('id', 'serial_number', 'title', 'description', 'owner')


@admin.register(Lesson)
class UserLesson(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'module', 'owner')
