# Generated by Django 5.1.5 on 2025-04-14 16:57

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GenericTest",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100)),
                (
                    "test_type",
                    models.CharField(
                        choices=[
                            ("daily_test", "DAILY_TEST"),
                            ("competition", "COMPETITION"),
                        ]
                    ),
                ),
                ("date_start", models.DateTimeField(auto_now_add=True)),
                ("date_end", models.DateTimeField()),
                ("image", models.CharField(blank=True, null=True)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
