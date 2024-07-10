from __future__ import annotations

from typing import TypedDict

from omu.app import App
from omu.client import Client
from omu.extension import Extension, ExtensionType
from omu.extension.endpoint import EndpointType
from omu.extension.table import TablePermissions, TableType
from omu.identifier import Identifier
from omu.network.packet import PacketType
from omu.serializer import Serializer

from .packets import (
    PermissionRequestPacket,
    PluginRequestPacket,
)

DASHBOARD_EXTENSION_TYPE = ExtensionType(
    "dashboard",
    lambda client: DashboardExtension(client),
    lambda: [],
)


class DashboardSetResponse(TypedDict):
    success: bool


DASHBOARD_SET_PERMISSION_ID = DASHBOARD_EXTENSION_TYPE / "set"
DASHBOARD_SET_ENDPOINT = EndpointType[Identifier, DashboardSetResponse].create_json(
    DASHBOARD_EXTENSION_TYPE,
    "set",
    request_serializer=Serializer.model(Identifier),
    permission_id=DASHBOARD_SET_PERMISSION_ID,
)
DASHBOARD_PERMISSION_REQUEST_PACKET = PacketType[
    PermissionRequestPacket
].create_serialized(
    DASHBOARD_EXTENSION_TYPE,
    "permission_request",
    serializer=PermissionRequestPacket,
)
DASHBOARD_PERMISSION_ACCEPT_PACKET = PacketType[str].create_json(
    DASHBOARD_EXTENSION_TYPE,
    "permission_accept",
)
DASHBOARD_PERMISSION_DENY_PACKET = PacketType[str].create_json(
    DASHBOARD_EXTENSION_TYPE,
    "permission_deny",
)
DASHBOARD_PLUGIN_REQUEST_PACKET = PacketType[PluginRequestPacket].create_serialized(
    DASHBOARD_EXTENSION_TYPE,
    "plugin_request",
    serializer=PluginRequestPacket,
)
DASHBOARD_PLUGIN_ACCEPT_PACKET = PacketType[str].create_json(
    DASHBOARD_EXTENSION_TYPE,
    "plugin_accept",
)
DASHBOARD_PLUGIN_DENY_PACKET = PacketType[str].create_json(
    DASHBOARD_EXTENSION_TYPE,
    "plugin_deny",
)
DASHBOARD_OPEN_APP_PERMISSION_ID = DASHBOARD_EXTENSION_TYPE / "app" / "open"
DASHBOARD_OPEN_APP_ENDPOINT = EndpointType[App, None].create_json(
    DASHBOARD_EXTENSION_TYPE,
    "open_app",
    request_serializer=Serializer.model(App),
    permission_id=DASHBOARD_OPEN_APP_PERMISSION_ID,
)
DASHBOARD_OPEN_APP_PACKET = PacketType[App].create_json(
    DASHBOARD_EXTENSION_TYPE,
    "open_app",
    Serializer.model(App),
)
DASHOBARD_APP_READ_PERMISSION_ID = DASHBOARD_EXTENSION_TYPE / "app" / "read"
DASHOBARD_APP_EDIT_PERMISSION_ID = DASHBOARD_EXTENSION_TYPE / "app" / "edit"
DASHBOARD_APP_TABLE_TYPE = TableType.create_model(
    DASHBOARD_EXTENSION_TYPE,
    "apps",
    App,
    permissions=TablePermissions(
        read=DASHOBARD_APP_READ_PERMISSION_ID,
        write=DASHOBARD_APP_EDIT_PERMISSION_ID,
        remove=DASHOBARD_APP_EDIT_PERMISSION_ID,
    ),
)


class DashboardExtension(Extension):
    def __init__(self, client: Client):
        self.client = client
        self.client.network.register_packet(
            DASHBOARD_PERMISSION_REQUEST_PACKET,
            DASHBOARD_PERMISSION_ACCEPT_PACKET,
            DASHBOARD_PERMISSION_DENY_PACKET,
            DASHBOARD_PLUGIN_REQUEST_PACKET,
            DASHBOARD_PLUGIN_ACCEPT_PACKET,
            DASHBOARD_PLUGIN_DENY_PACKET,
            DASHBOARD_OPEN_APP_PACKET,
        )
        self.apps = client.tables.get(DASHBOARD_APP_TABLE_TYPE)

    async def open_app(self, app: App) -> None:
        if not self.client.permissions.has(DASHBOARD_OPEN_APP_PERMISSION_ID):
            error = f"Pemission {DASHBOARD_OPEN_APP_PERMISSION_ID} required to open app {app}"
            raise PermissionError(error)
        await self.client.endpoints.call(DASHBOARD_OPEN_APP_ENDPOINT, app)
