from dataclasses import dataclass, field

@dataclass
class PlayerState:
    name: str
    life: int = 40
    commander_tax: int = 0
    hand: list[str] = field(default_factory=list)
    library: list[str] = field(default_factory=list)
    battlefield: list[str] = field(default_factory=list)
    graveyard: list[str] = field(default_factory=list)
    exile: list[str] = field(default_factory=list)
    command_zone: list[str] = field(default_factory=list)

@dataclass
class GameState:
    players: list[PlayerState] = field(default_factory=list)
    active_player: int = 0
    turn_number: int = 1
