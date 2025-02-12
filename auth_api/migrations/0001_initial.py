# Generated by Django 5.1.5 on 2025-02-02 16:31

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("username", models.CharField(max_length=25)),
                (
                    "email",
                    models.EmailField(
                        max_length=255, unique=True, verbose_name="Email"
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("password", models.CharField(max_length=255)),
                ("dob", models.DateField(null=True)),
                ("phone", models.CharField(max_length=15, null=True)),
                ("image", models.CharField(max_length=2555, null=True)),
                ("is_active", models.BooleanField(default=False)),
                ("is_deleted", models.BooleanField(default=False)),
                ("is_admin", models.BooleanField(default=False)),
                ("is_staff", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="UserEmailVerification",
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
                ("code", models.CharField(max_length=6)),
                ("expiration_time", models.DateTimeField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="auth_api.user"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
