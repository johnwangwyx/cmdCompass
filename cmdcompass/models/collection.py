from dataclasses import dataclass
from typing import List

from cmdcompass.models.command import Command

@dataclass
class Collection:
    name: str
    commands: List[Command]