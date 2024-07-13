from __future__ import annotations

import os

from pylav.extension.m3u.parser import is_url, urljoin


def _urijoin(base_uri: str, path: str) -> str:
    if not is_url(base_uri):
        return os.path.normpath(os.path.join(base_uri, path.strip("/")))
    if base_uri[-1] != "/":
        base_uri += "/"
    return urljoin(base_uri, path)


class BasePathMixin:
    __slots__ = ("base_uri", "uri")
    base_uri: str | None
    uri: str | None

    @property
    def absolute_uri(self) -> str | None:
        if self.uri is None:
            return None
        if is_url(self.uri):
            return self.uri
        if self.base_uri is None:
            raise ValueError("There can not be `absolute_uri` with no `base_uri` set")
        return _urijoin(self.base_uri, self.uri)

    @property
    def base_path(self) -> str | None:
        return None if self.uri is None else os.path.dirname(self.get_path_from_uri())

    def get_path_from_uri(self) -> str:
        """Some URIs have a slash in the query string"""
        return self.uri.split("?")[0]

    @base_path.setter
    def base_path(self, newbase_path: str) -> None:
        if self.uri is not None:
            self.uri = (
                self.uri.replace(self.base_path, newbase_path) if self.base_path else f"{newbase_path}/{self.uri}"
            )


class GroupedBasePathMixin:
    __slots__ = ()

    def _set_base_uri(self, new_base_uri: str) -> None:
        for item in self:  # type: ignore
            item.base_uri = new_base_uri

    base_uri = property(None, _set_base_uri)

    def _set_base_path(self, newbase_path: str) -> None:
        for item in self:  # type: ignore
            item.base_path = newbase_path

    base_path = property(None, _set_base_path)
