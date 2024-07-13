from dcim.models import Device
from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel

from netbox_swupdate.utils import generate_uuid

from .deploy import Deploy

__all__ = ["FirmwareRequest"]


class FirmwareRequest(NetBoxModel):
    DEPLOY_STATUS_DEVICE = [
        (0, "STARTED"),
        (1, "FINISHED"),
        (2, "FAILED"),
    ]
    RETRY_CHOICES = [
        (0, "0"),
        (2, "2"),
        (4, "4"),
        (6, "6"),
        (10, "10"),
        (20, "20"),
    ]

    RETRY_INTERVAL_CHOICES = [
        (0, "0 minutes"),
        (1, "1 minutes"),
        (2, "2 minutes"),
        (5, "5 minutes"),
    ]
    firmware_request_id = models.UUIDField(
        default=generate_uuid, editable=False, unique=True
    )
    deploy_time = models.DateTimeField(
        blank=True,
        null=True,
        help_text="Fecha y hora de la solicitud de actualización.",
    )
    device = models.ForeignKey(
        Device,
        on_delete=models.CASCADE,
        help_text="Dispositivos a los que afectará el despliegue",
    )
    deploy = models.ForeignKey(
        Deploy, on_delete=models.CASCADE, help_text="Deploy del dispositivo."
    )
    status = models.CharField(
        max_length=50,
        choices=DEPLOY_STATUS_DEVICE,
        help_text="Estado del despliegue",
        default=0,
    )
    retries = models.IntegerField(
        choices=RETRY_CHOICES,
        default=0,
        help_text="Número de reintentos permitidos para el despliegue.",
    )
    retry_interval = models.IntegerField(
        choices=RETRY_INTERVAL_CHOICES,
        default=0,
        help_text="Tiempo mínimo entre reintentos, en minutos.",
    )

    class Meta:
        ordering = ("pk",)

    def get_absolute_url(self):
        return reverse("plugins:netbox_swupdate:firmware_request", args=[self.pk])
