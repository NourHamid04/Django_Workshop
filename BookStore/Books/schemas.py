from ninja import Schema

class AuthorSchema(Schema):
    id: int
    name: str

class AuthorCreateSchema(Schema):
    name: str

class BookSchema(Schema):
    id: int
    title: str
    description: str
    author: AuthorSchema

class BookCreateSchema(Schema):
    title: str
    description: str
    author_id:int