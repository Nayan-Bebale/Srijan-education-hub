# Generated by Django 5.0.2 on 2024-02-15 11:21

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                ("course_id", models.AutoField(primary_key=True, serialize=False)),
                ("course_name", models.CharField(max_length=255)),
                ("instructor", models.CharField(max_length=255)),
                ("video_url", models.URLField()),
                ("course_image", models.URLField()),
                ("course_description", ckeditor.fields.RichTextField()),
                (
                    "review_avg",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=3),
                ),
                ("review_count", models.PositiveIntegerField(default=0)),
                ("course_duration", models.DurationField()),
                (
                    "level",
                    models.CharField(
                        choices=[
                            ("Beginner", "Beginner"),
                            ("Intermediate", "Intermediate"),
                            ("Advanced", "Advanced"),
                            ("All", "All"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "discount_price",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                (
                    "original_price",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("student_count", models.PositiveIntegerField(default=0)),
            ],
        ),
    ]