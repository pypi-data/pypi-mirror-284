from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from netbox_swupdate.models import Deploy
from netbox_swupdate.permissions import IsDeviceAuthenticated

__all__ = ("RouteDownloadView",)


class RouteDownloadView(APIView):
    """Download firmware."""

    permission_classes = [IsDeviceAuthenticated]

    # def route_download(request, filepath):
    #     """
    #     Maneja la descarga de archivos de firmware desde la instancia de SWUpdate.
    #
    #     Args:
    #         request (HttpRequest): La solicitud HTTP entrante.
    #         filepath (str): La ruta del archivo de firmware solicitado.
    #
    #     Returns:
    #         HttpResponse: La respuesta HTTP que contiene el archivo de firmware o un mensaje de error.
    #     """
    #     try:
    #         # Realiza una solicitud GET a la API de SWUpdate para obtener el archivo de firmware
    #         response = requests.get(f"{SWUPDATE_URL}/firmware/{filepath}", stream=True)
    #     except requests.exceptions.RequestException as e:
    #         # Maneja cualquier error de conexión con la API de SWUpdate
    #         return HttpResponse(
    #             f"500 Error connecting to SWUpdate: {e}",
    #             status=500,
    #             content_type="text/plain; charset=utf-8",
    #         )
    #
    #     if response.status_code == 200:
    #         # Si la solicitud tiene éxito, devuelve el contenido del archivo de firmware
    #         return HttpResponse(
    #             response.content, content_type="application/octet-stream"
    #         )
    #     else:
    #         # Si hay algún error (por ejemplo, archivo no encontrado), devuelve el mensaje de error
    #         return HttpResponse(
    #             response.content,
    #             status=response.status_code,
    #             content_type=response.headers.get(
    #                 "Content-Type", "text/plain; charset=utf-8"
    #             ),
    #         )

    def get(self, request):
        device = request.device
        if device:
            # - buscar en deploy si ese dispositivo tiene actualizaciones.
            #     - Se busca por ID y por fecha.
            #     - Se verifica si el Device ya ha sido actualizado con el deploy configurado.
            #     - Se verifica el estado con el que termino el deploy.
            pass
        else:
            pass
