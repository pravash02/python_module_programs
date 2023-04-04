import json
import pydantic
from typing import Optional, List


class Book(pydantic.BaseModel):
    title: str
    author: str
    publisher: str
    publishing_no: Optional[str]
    verification_no: Optional[str]
    subtitle: Optional[str]

    @pydantic.root_validator(pre=True)
    @classmethod
    def check_publishing_or_verification(cls, values):
        if "publishing_no" not in values and "verification_no" not in values:
            raise Exception("Document should have either an publishing_no or verification_no")
        return values

    @pydantic.validator("verification_no")
    @classmethod
    def verification_no_valid(cls, value):
        chars = [c for c in value if c.startswith('978')]
        return value

    class Config:
        allow_mutation = False
        anystr_lower = True


def main():
    with open("./data.json") as file:
        data = json.load(file)
        books: List[Book] = [Book(**item) for item in data]
        print(books[0].dict())


if __name__ == "__main__":
    main()
