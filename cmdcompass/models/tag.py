from dataclasses import dataclass, field
import uuid

@dataclass
class Tag:
    name: str
    color: str
    uuid: str = field(default_factory=lambda: str(uuid.uuid4()))