from LSP.plugin import AbstractPlugin, register_plugin, unregister_plugin
from LSP.plugin.core.protocol import Location
from LSP.plugin.core.typing import Any, Callable, List, Mapping
from LSP.plugin.locationpicker import LocationPicker
import sublime


SESSION_NAME = "mdita-marksman"


class MditaMarksman(AbstractPlugin):
    @classmethod
    def name(cls) -> str:
        return SESSION_NAME

    @classmethod
    def needs_update_or_installation(cls) -> bool:
        return False

    def on_pre_server_command(self, command: Mapping[str, Any], done_callback: Callable[[], None]) -> bool:
        command_name = command['command']
        if command_name == 'marksman.findReferences':
            command_arguments = command['arguments']
            if command_arguments and 'locations' in command_arguments[0]:
                self._handle_show_references(command_arguments[0]['locations'])
            done_callback()
            return True
        return False

    def _handle_show_references(self, references: List[Location]) -> None:
        session = self.weaksession()
        if not session:
            return
        view = sublime.active_window().active_view()
        if not view:
            return
        if len(references) == 1:
            args = {
                'location': references[0],
                'session_name': session.config.name,
            }
            window = view.window()
            if window:
                window.run_command('lsp_open_location', args)
        elif references:
            LocationPicker(view, session, references, side_by_side=False)
        else:
            sublime.status_message('No references found')


def plugin_loaded() -> None:
    register_plugin(MditaMarksman)


def plugin_unloaded() -> None:
    unregister_plugin(MditaMarksman)
