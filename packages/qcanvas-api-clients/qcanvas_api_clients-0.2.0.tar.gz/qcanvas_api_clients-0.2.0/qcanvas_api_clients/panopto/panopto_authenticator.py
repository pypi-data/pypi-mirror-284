import logging

from qcanvas_api_clients.canvas.canvas_client import CanvasClient
from qcanvas_api_clients.panopto.panopto_client_config import PanoptoClientConfig
from qcanvas_api_clients.util.authenticator import Authenticator


class PanoptoAuthenticator(Authenticator):
    _logger = logging.getLogger(__name__)

    def __init__(
        self, panopto_client_config: PanoptoClientConfig, canvas_client: CanvasClient
    ):
        super().__init__(canvas_client._client)
        self._panopto_client_config = panopto_client_config
        self._canvas_client = canvas_client

    async def _authenticate(self) -> None:
        self._logger.debug("Authenticating to panopto")

        response = await self._canvas_client.authenticate_panopto(
            self._panopto_client_config.get_endpoint(
                "Panopto/Pages/Auth/Login.aspx?instance=Canvas&AllowBounce=true"
            )
        )

        response.raise_for_status()
        self._logger.debug("Authentication complete")
