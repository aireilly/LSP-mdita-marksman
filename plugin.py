import os
import shutil

from LSP.plugin import AbstractPlugin, register_plugin, unregister_plugin

SESSION_NAME = "mdita-marksman"


def _find_binary():
    """Locate the mdita-marksman binary on the system."""
    candidates = [
        os.path.expanduser("~/.local/bin/mdita-marksman"),
        "/usr/local/bin/mdita-marksman",
        "/usr/bin/mdita-marksman",
    ]
    for path in candidates:
        if os.path.isfile(path) and os.access(path, os.X_OK):
            return path
    return shutil.which("mdita-marksman")


class MditaMarksman(AbstractPlugin):
    @classmethod
    def name(cls) -> str:
        return SESSION_NAME

    @classmethod
    def basedir(cls) -> str:
        return os.path.join(cls.storage_path(), __package__)

    @classmethod
    def install_or_update(cls) -> None:
        binary = _find_binary()
        if binary is None:
            raise RuntimeError(
                "mdita-marksman binary not found. "
                "Install it from https://github.com/aireilly/mdita-marksman "
                "and ensure it is available on your PATH or in ~/.local/bin."
            )


def plugin_loaded() -> None:
    register_plugin(MditaMarksman)


def plugin_unloaded() -> None:
    unregister_plugin(MditaMarksman)
