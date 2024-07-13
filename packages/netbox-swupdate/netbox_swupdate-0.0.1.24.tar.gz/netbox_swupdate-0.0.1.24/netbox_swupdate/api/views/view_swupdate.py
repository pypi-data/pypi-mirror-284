from django.contrib.sites import requests
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView

from netbox_swupdate.models import Deploy, FirmwareRequest
from netbox_swupdate.permissions import IsDeviceAuthenticated

__all__ = ("RouteDownloadView",)


class RouteDownloadView(APIView):
    """Download firmware."""

    permission_classes = [IsDeviceAuthenticated]

    def _send_to_device(self):
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

    def get(self, request):
        device = request.device
        if device:
            deploy_updates = Deploy.objects.get(
                devices__id=device.id, state__in=["INITIATED", "STOPPED"]
            )
            if deploy_updates:
                firmware_request = FirmwareRequest.objects.get(
                    deploy=deploy_updates, device__id=device.id
                )
                if firmware_request:
                    if firmware_request.status == "FINISHED":
                        return JsonResponse(
                            {"data": "Device updated successfully."}, status=200
                        )
                    elif firmware_request.status == "STARTED":
                        return JsonResponse({"data": "Device updating."}, status=200)
                    elif firmware_request.status == "FAILED":
                        pass
                else:
                    pass
        return JsonResponse({"error": "No update."}, status=400)
