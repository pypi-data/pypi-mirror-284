"""Top-level package for NetBox SWUpdate Plugin."""

__author__ = """Óscar Hurtado"""
__email__ = "ohurtadp@sens.solutions"
__version__ = "0.0.1.18"


import uuid

from dcim.models import Device
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from extras.models import CustomField, CustomFieldTypeChoices
from netbox.plugins import PluginConfig


class SWUpdateConfig(PluginConfig):
    name = "netbox_swupdate"
    verbose_name = "NetBox SWUpdate Plugin"
    description = "NetBox plugin for SWUpdate."
    version = __version__
    author = __author__
    author_email = __email__
    base_url = "netbox_swupdate"
    required_settings = []
    default_settings = {
        "SWUPDATE_TIMEOUT": 30,
        "SWUPDATE_ARGS": {},
    }

    def ready(self):
        @receiver(post_migrate)
        def create_custom_field(sender, **kwargs):
            field, created = CustomField.objects.get_or_create(
                name="token",
                type=CustomFieldTypeChoices.TYPE_TEXT,
                defaults={
                    "default": lambda: str(
                        uuid.uuid4()
                    ),  # Genera un UUID como valor por defecto
                    "label": "Token",
                },
            )
            if created:
                field.content_types.set([Device])


config = SWUpdateConfig
