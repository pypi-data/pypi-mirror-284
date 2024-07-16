from datetime import datetime

from dcim.models import Device
from django.contrib.auth.models import AnonymousUser
from django.contrib.sites import requests
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView

from netbox_swupdate.models import Deploy, FirmwareRequest
from netbox_swupdate.permissions import IsDeviceAuthenticated

__all__ = ("RouteDownloadView",)


class RouteDownloadView(APIView):
    """Download firmware."""

    permission_classes = [IsDeviceAuthenticated]

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            request.user = AnonymousUser()
        return super(RouteDownloadView, self).dispatch(request, *args, **kwargs)

    def _send_to_device(self, requests):
        try:
            repository_host: str = ""
            file_path: str = ""
            # Necesito la ruta del repositorio de la imagen .SW
            response = requests.get(
                f"{repository_host}/firmware/{file_path}", stream=True
            )
        except requests.exceptions.RequestException as e:
            # Maneja cualquier error de conexión con la API de SWUpdate
            return HttpResponse(
                f"500 Error connecting to SWUpdate: {e}",
                status=500,
                content_type="text/plain; charset=utf-8",
            )

        if response.status_code == 200:
            return HttpResponse(
                response.content, content_type="application/octet-stream"
            )
        else:
            return HttpResponse(
                response.content,
                status=response.status_code,
                content_type=response.headers.get(
                    "Content-Type", "text/plain; charset=utf-8"
                ),
            )

    def _register_device_update(self, device: Device, deploy: Deploy):
        firmware_request = FirmwareRequest.objects.create(
            device=device,
            deploy=deploy,
            deploy_time=datetime.now(),
            status=FirmwareRequest.DEPLOY_STATUS_DEVICE[0][0],  # Estado "STARTED"
            retries=0,
        )

    def _allow_update(self, firmware_request: FirmwareRequest) -> bool:
        """
        This method has the function of evaluating whether a new update can be
        performed based on different restrictions: time between update requests,
        number of update attempts.
        """
        firmware_request.status = FirmwareRequest.DEPLOY_STATUS_DEVICE[2][0]
        firmware_request.save()

    def _update_update_status(self, firmware_request: FirmwareRequest):
        if self._allow_update(firmware_request=firmware_request):
            firmware_request.status = FirmwareRequest.DEPLOY_STATUS_DEVICE[0][0]
            firmware_request.deploy_time = datetime.now()
            firmware_request.retries += 1
            firmware_request.save()

    def get(self, request):
        device = request.device
        if device:
            deploy_updates = Deploy.objects.get(
                devices__id=device.id, state__in=["INITIATED", "STOPPED"]
            )
            if deploy_updates:
                try:
                    firmware_request = FirmwareRequest.objects.get(
                        deploy=deploy_updates, device__id=device.id
                    )
                except FirmwareRequest.DoesNotExist:
                    firmware_request = None
                if firmware_request:
                    if firmware_request.status == "FINISHED":
                        return JsonResponse(
                            {
                                "data": f"Device updated successfully: {firmware_request.deploy_time}."
                            },
                            status=200,
                        )
                    elif firmware_request.status == "STARTED":
                        # Aqui establecemos un max de started.
                        return JsonResponse({"data": "Device updating."}, status=200)
                    elif firmware_request.status == "FAILED":
                        self._update_update_status(firmware_request=firmware_request)
                else:
                    self._register_device_update(device=device, deploy=deploy_updates)
        return JsonResponse({"error": "No update."}, status=400)
