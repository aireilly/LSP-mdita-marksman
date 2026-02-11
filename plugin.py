from LSP.plugin import AbstractPlugin, register_plugin, unregister_plugin


SESSION_NAME = "mdita-marksman"


class MditaMarksman(AbstractPlugin):
    @classmethod
    def name(cls) -> str:
        return SESSION_NAME

    @classmethod
    def needs_update_or_installation(cls) -> bool:
        return False


def plugin_loaded() -> None:
    register_plugin(MditaMarksman)


def plugin_unloaded() -> None:
    unregister_plugin(MditaMarksman)
