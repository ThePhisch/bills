from dataclasses import dataclass
from datetime import datetime

@dataclass
class Bill:
    name: str
    datetime: datetime