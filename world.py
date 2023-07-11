from dataclasses import dataclass, field


@dataclass
class Area:
    name: str = ""
    description: str = ""
    available_directions: list = field(default_factory=list)
    enemies: list = field(default_factory=list)
    treasures: list = field(default_factory=list)
    npcs: list = field(default_factory=list)
    visited: bool = False


class Shop:
    pass
