from __future__ import annotations

import asyncio

from loguru import logger

from omu.address import Address
from omu.app import App
from omu.event_emitter import Unlisten
from omu.extension import ExtensionRegistry
from omu.extension.asset import (
    ASSET_EXTENSION_TYPE,
    AssetExtension,
)
from omu.extension.dashboard import (
    DASHBOARD_EXTENSION_TYPE,
    DashboardExtension,
)
from omu.extension.endpoint import (
    ENDPOINT_EXTENSION_TYPE,
    EndpointExtension,
)
from omu.extension.i18n import (
    I18N_EXTENSION_TYPE,
    I18nExtension,
)
from omu.extension.logger import (
    LOGGER_EXTENSION_TYPE,
    LoggerExtension,
)
from omu.extension.permission import (
    PERMISSION_EXTENSION_TYPE,
    PermissionExtension,
)
from omu.extension.plugin import (
    PLUGIN_EXTENSION_TYPE,
    PluginExtension,
)
from omu.extension.registry import (
    REGISTRY_EXTENSION_TYPE,
    RegistryExtension,
)
from omu.extension.server import (
    SERVER_EXTENSION_TYPE,
    ServerExtension,
)
from omu.extension.signal import (
    SIGNAL_EXTENSION_TYPE,
    SignalExtension,
)
from omu.extension.table import (
    TABLE_EXTENSION_TYPE,
    TableExtension,
)
from omu.helper import Coro
from omu.network import Network
from omu.network.packet import Packet, PacketType
from omu.network.websocket_connection import WebsocketsConnection
from omu.token import JsonTokenProvider, TokenProvider

from .client import Client, ClientEvents


class Omu(Client):
    def __init__(
        self,
        app: App,
        address: Address | None = None,
        token: TokenProvider | None = None,
        connection: WebsocketsConnection | None = None,
        extension_registry: ExtensionRegistry | None = None,
        loop: asyncio.AbstractEventLoop | None = None,
    ):
        self._loop = loop or asyncio.get_event_loop()
        self._ready = False
        self._running = False
        self._event = ClientEvents()
        self._app = app
        self.address = address or Address("127.0.0.1", 26423)
        self._network = Network(
            self,
            self.address,
            token or JsonTokenProvider(),
            connection or WebsocketsConnection(self, self.address),
        )
        self._extensions = extension_registry or ExtensionRegistry(self)

        self._endpoints = self.extensions.register(ENDPOINT_EXTENSION_TYPE)
        self._plugins = self.extensions.register(PLUGIN_EXTENSION_TYPE)
        self._tables = self.extensions.register(TABLE_EXTENSION_TYPE)
        self._registry = self.extensions.register(REGISTRY_EXTENSION_TYPE)
        self._signal = self.extensions.register(SIGNAL_EXTENSION_TYPE)
        self._permissions = self.extensions.register(PERMISSION_EXTENSION_TYPE)
        self._server = self.extensions.register(SERVER_EXTENSION_TYPE)
        self._assets = self.extensions.register(ASSET_EXTENSION_TYPE)
        self._dashboard = self.extensions.register(DASHBOARD_EXTENSION_TYPE)
        self._i18n = self.extensions.register(I18N_EXTENSION_TYPE)
        self._logger = self.extensions.register(LOGGER_EXTENSION_TYPE)

    @property
    def ready(self) -> bool:
        return self._ready

    @property
    def app(self) -> App:
        return self._app

    @property
    def loop(self) -> asyncio.AbstractEventLoop:
        return self._loop

    @property
    def network(self) -> Network:
        return self._network

    @property
    def extensions(self) -> ExtensionRegistry:
        return self._extensions

    @property
    def endpoints(self) -> EndpointExtension:
        return self._endpoints

    @property
    def plugins(self) -> PluginExtension:
        return self._plugins

    @property
    def tables(self) -> TableExtension:
        return self._tables

    @property
    def registry(self) -> RegistryExtension:
        return self._registry

    @property
    def signal(self) -> SignalExtension:
        return self._signal

    @property
    def assets(self) -> AssetExtension:
        return self._assets

    @property
    def server(self) -> ServerExtension:
        return self._server

    @property
    def permissions(self) -> PermissionExtension:
        return self._permissions

    @property
    def dashboard(self) -> DashboardExtension:
        return self._dashboard

    @property
    def i18n(self) -> I18nExtension:
        return self._i18n

    @property
    def logger(self) -> LoggerExtension:
        return self._logger

    @property
    def running(self) -> bool:
        return self._running

    async def send[T](self, type: PacketType[T], data: T) -> None:
        await self._network.send(Packet(type, data))

    def run(self, *, reconnect: bool = True) -> None:
        try:
            self.loop.set_exception_handler(self.handle_exception)
            self.loop.create_task(self.start(reconnect=reconnect))
            self.loop.run_forever()
        finally:
            self.loop.close()
            asyncio.run(self.stop())

    def handle_exception(self, loop: asyncio.AbstractEventLoop, context: dict) -> None:
        logger.error(context["message"])
        exception = context.get("exception")
        if exception:
            raise exception

    async def start(self, *, reconnect: bool = True) -> None:
        if self._running:
            raise RuntimeError("Already running")
        self._running = True
        self.loop.create_task(self._network.connect(reconnect=reconnect))
        await self._event.started()

    async def stop(self) -> None:
        if not self._running:
            raise RuntimeError("Not running")
        self._running = False
        await self._network.disconnect()
        await self._event.stopped()

    @property
    def event(self) -> ClientEvents:
        return self._event

    def on_ready(self, coro: Coro[[], None]) -> Unlisten:
        if self._ready:
            self.loop.create_task(coro())
        return self.event.ready.listen(coro)
