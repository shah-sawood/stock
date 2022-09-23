from django.apps import AppConfig


class ShopConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "shop"

    def ready(self):
        """Implicitly connect signal handlers decorated with @receiver."""
        from . import signals
