from django.db import models

from config import settings

NULLABLE = {"null": True, "blank": True}


class Module(models.Model):
    serial_number = models.PositiveIntegerField(verbose_name="Порядковый номер учебного модуля")
    title = models.CharField(max_length=100, verbose_name="Название учебного модуля")

    description = models.TextField(verbose_name="Описание модуля", **NULLABLE)

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Создатель учебного модуля",
        **NULLABLE
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Модуль"
        verbose_name_plural = "Модули"


class Lesson(models.Model):
    title = models.CharField(
        max_length=100, verbose_name="Название урока", help_text="Укажите название урока"
    )

    description = models.TextField(verbose_name="Описание урока", **NULLABLE)

    preview = models.ImageField(upload_to="modules/lessons", **NULLABLE)

    url = models.URLField(verbose_name="Ccылка на видео", **NULLABLE)

    module = models.ForeignKey(
        Module, on_delete=models.SET_NULL, verbose_name="Модуль", **NULLABLE
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Создатель урока",
        **NULLABLE
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
