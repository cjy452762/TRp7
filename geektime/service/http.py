import dataclasses


@dataclasses
class Request:
    method: str = None
    host: str = None
    path: str = None
    query: dict = None
    json: dict = None
    data: dict = None
