from __future__ import annotations

import logging
from collections.abc import Collection
from typing import TYPE_CHECKING, ClassVar

from attrs import define, field
from typing_extensions import Self

from cloudshell.cli.configurator import AbstractModeConfigurator
from cloudshell.cli.factory.session_factory import (
    CloudInfoAccessKeySessionFactory,
    ConsoleSessionFactory,
    GenericSessionFactory,
    SessionFactory,
)
from cloudshell.cli.service.command_mode_helper import CommandModeHelper
from cloudshell.cli.session.console_ssh import ConsoleSSHSession
from cloudshell.cli.session.console_telnet import ConsoleTelnetSession

from cloudshell.raritan.cli.raritan_command_modes import (
    ConfigCommandMode,
    EnableCommandMode,
)
from cloudshell.raritan.cli.raritan_ssh_session import RaritanSSHSession
from cloudshell.raritan.cli.raritan_telnet_session import RaritanTelnetSession

if TYPE_CHECKING:
    from cloudshell.cli.service.cli import CLI
    from cloudshell.cli.types import T_COMMAND_MODE_RELATIONS, CliConfigProtocol


@define
class RaritanCliConfigurator(AbstractModeConfigurator):
    REGISTERED_SESSIONS: ClassVar[tuple[SessionFactory]] = (
        CloudInfoAccessKeySessionFactory(RaritanSSHSession),
        GenericSessionFactory(RaritanTelnetSession),
        ConsoleSessionFactory(ConsoleSSHSession),
        ConsoleSessionFactory(
            ConsoleTelnetSession, session_kwargs={"start_with_new_line": False}
        ),
        ConsoleSessionFactory(
            ConsoleTelnetSession, session_kwargs={"start_with_new_line": True}
        ),
    )
    modes: T_COMMAND_MODE_RELATIONS = field(init=False)

    def __attrs_post_init__(self):
        super().__attrs_post_init__()
        self.modes = CommandModeHelper.create_command_mode(self._auth)

    @classmethod
    def from_config(
        cls,
        conf: CliConfigProtocol,
        logger: logging.Logger | None = None,
        cli: CLI | None = None,
        registered_sessions: Collection[SessionFactory] | None = None,
    ) -> Self:
        if not logger:
            logger = logging.getLogger(__name__)
        return super().from_config(conf, logger, cli, registered_sessions)

    @property
    def enable_mode(self):
        return self.modes[EnableCommandMode]

    @property
    def config_mode(self):
        return self.modes[ConfigCommandMode]
