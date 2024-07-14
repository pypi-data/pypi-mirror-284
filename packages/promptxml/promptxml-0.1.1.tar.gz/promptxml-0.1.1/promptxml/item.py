from typing import Iterable, Self
from xml.sax.saxutils import escape


class PromptItem:
    def __init__(self, *, label: str, value: str) -> None:
        self.label = label
        self.value = value

    def to_xml(self) -> str:
        return f"<{self.label}>{escape(self.value, entities={})}</{self.label}>"

    @classmethod
    def build_multiple(cls, *, label: str, values: Iterable[str]) -> list[Self]:
        return [cls(label=label, value=v) for v in values]
