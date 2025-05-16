from dataclasses import dataclass, field
import uuid

@dataclass
class Contact:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str = ""
    phone: str = ""
    email: str = ""
