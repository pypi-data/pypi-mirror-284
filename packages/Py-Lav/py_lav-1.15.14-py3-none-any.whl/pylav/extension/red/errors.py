from __future__ import annotations

from redbot.core import commands

from pylav.core.context import PyLavContext


class IncompatibleException(EnvironmentError):
    """Command raised when an incompatible cog is already loaded"""


class MediaPlayerError(commands.CommandError):
    """
    Base class for all media player errors.
    """


class UnauthorizedChannelError(MediaPlayerError):
    """
    Raised when a command is used in a channel that is not authorized.
    """

    def __init__(self, channel: int):
        self.channel = channel


class MediaPlayerCheckError(MediaPlayerError):
    """
    Base class for all check errors.
    """


class MediaPlayerNotFoundError(MediaPlayerCheckError, commands.CheckFailure):
    """
    Raised when a media player is not found.
    """

    def __init__(self, context: PyLavContext) -> None:
        self.context = context


class NotDJError(MediaPlayerCheckError, commands.CheckFailure):
    """
    Raised when user does not have DJ Perms.
    """

    def __init__(self, context: PyLavContext) -> None:
        self.context = context
