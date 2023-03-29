from django.apps import AppConfig


class AsDjangoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "as_django"
