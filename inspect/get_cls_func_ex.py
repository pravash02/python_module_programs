import dataclasses
import inspect
from dataclasses import dataclass, field


@dataclass(frozen=True, order=True)
class Comment:
    id: int
    text: str = ""
    replies: list[int] = field(default_factory=list, repr=False, compare=False)


comment = Comment(1, "I just subscribed!")
print(inspect.getmembers(Comment, inspect.isfunction))
