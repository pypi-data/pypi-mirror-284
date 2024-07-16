from __future__ import annotations

from typing import TYPE_CHECKING

from cloudshell.cli.session.telnet_session import TelnetSession

if TYPE_CHECKING:
    from logging import Logger

    from cloudshell.cli.types import T_ACTION_MAP


class RaritanTelnetSession(TelnetSession):
    def _connect_action_map(self) -> T_ACTION_MAP:
        am = super()._connect_action_map
        cli_action_key = r"Restricted Service Agreement"

        def action(session: RaritanTelnetSession, sess_logger: Logger) -> None:
            session.send_line("y", sess_logger)
            del am[cli_action_key]

        am[cli_action_key] = action

        return am
