from dataclasses import dataclass
from enum import StrEnum

from stampy.input import promptable


@dataclass
class BirthdayContext:
    name: str
    display_name: str
    birthday: str
    email_address: str
    mailing_address: str


@dataclass
class SenderContext:
    name: str
    email_address: str


@promptable
class Action(StrEnum):
    SKIP = "SKIP"
    CARD = "CARD"
    EMAIL = "EMAIL"


@promptable
class EmailAction(StrEnum):
    SEND = "SEND"
    # TODO rename to be clearer
    DRAFT = "DRAFT"
    DISCARD = "DISCARD"
