from netbox.forms import NetBoxModelForm

from netbox_swupdate.models import FirmwareRequest

__all__ = ("FirmwareRequestForm",)


class FirmwareRequestForm(NetBoxModelForm):
    class Meta:
        model = FirmwareRequest
        fields = ["firmware_request_id", "deploy_time", "device", "deploy", "status"]
