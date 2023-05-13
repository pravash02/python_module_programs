@dataclass
class Piece:
    x: int
    y: int
    color: Color = Color. NONE
    type: PieceType = PieceType.EMPTY

    @classmethod
    def from_fen(cls: Type[Piece], x: int, y: int, fen: str) -> Self:
        color = Color.WhITE if fen.isupper() else Color. BLACK
        return cls(x, y, color, type=FEN_MAP [fen.lower()])