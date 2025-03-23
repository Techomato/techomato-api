from django.apps import AppConfig


class GenericTestConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "generic_test"
