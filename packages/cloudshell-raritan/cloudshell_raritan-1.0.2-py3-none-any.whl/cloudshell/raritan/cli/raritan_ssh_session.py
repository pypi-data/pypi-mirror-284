from __future__ import annotations

from typing import TYPE_CHECKING

from cloudshell.cli.session.ssh_session import SSHSession

if TYPE_CHECKING:
    from logging import Logger


class RaritanSSHSession(SSHSession):
    def _connect_actions(self, prompt: str, logger: Logger) -> None:
        action_map = {}
        cli_action_key = r"Restricted Service Agreement"

        def action(session: RaritanSSHSession, sess_logger: Logger) -> None:
            session.send_line("y", sess_logger)
            del action_map[cli_action_key]

        action_map[cli_action_key] = action
        self.hardware_expect(
            None,
            expected_string=prompt,
            action_map=action_map,
            timeout=self._timeout,
            logger=logger,
        )
        self._on_session_start(logger)
