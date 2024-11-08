# Generated by Django 5.1.2 on 2024-10-31 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Lesson",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Укажите название урока",
                        max_length=100,
                        verbose_name="Название урока",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, null=True, verbose_name="Описание урока"
                    ),
                ),
                (
                    "preview",
                    models.ImageField(
                        blank=True, null=True, upload_to="modules/lessons"
                    ),
                ),
                (
                    "url",
                    models.URLField(
                        blank=True, null=True, verbose_name="Ccылка на видео"
                    ),
                ),
            ],
            options={
                "verbose_name": "Урок",
                "verbose_name_plural": "Уроки",
            },
        ),
        migrations.CreateModel(
            name="Module",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "serial_number",
                    models.PositiveIntegerField(
                        verbose_name="Порядковый номер учебного модуля"
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=100, verbose_name="Название учебного модуля"
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, null=True, verbose_name="Описание модуля"
                    ),
                ),
            ],
            options={
                "verbose_name": "Модуль",
                "verbose_name_plural": "Модули",
            },
        ),
    ]
