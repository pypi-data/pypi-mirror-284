import xml.dom.minidom
from typing import Iterable, Self, Union
from xml.sax.saxutils import quoteattr

from promptxml.item import PromptItem


class PromptSection:
    def __init__(
        self, *, label: str, items: Iterable[Union[PromptItem, Self]] | None = None, **attributes: str
    ) -> None:
        self.label = label
        self._items: list[Union[PromptItem, Self]] = list(items or [])
        self._attributes: dict[str, str] = attributes

    def add(self, *items: PromptItem | Self) -> None:
        if not all(isinstance(item, (PromptItem, PromptSection)) for item in items):
            raise ValueError("All items must be either PromptItem or PromptSection")

        self._items.extend(items)

    def to_xml(self) -> str:
        value = "".join(i.to_xml() for i in self._items)
        if len(self._attributes) == 0:
            return f"<{self.label}>{value}</{self.label}>"

        attributes = " ".join(f"{k}={quoteattr(v, entities={})}" for k, v in self._attributes.items())

        return f"<{self.label} {attributes}>{value}</{self.label}>"

    def make_pretty(self, indent: str = "  ") -> str:
        _xml = self.to_xml()

        dom = xml.dom.minidom.parseString(_xml)
        pretty_xml = dom.toprettyxml(indent=indent)
        pretty_xml = "\n".join(
            line for line in pretty_xml.split("\n") if line.strip() and line.strip() != '<?xml version="1.0" ?>'
        )

        return pretty_xml
