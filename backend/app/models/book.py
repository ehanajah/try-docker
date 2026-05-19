def serialize_book(book):
    return {
        "id": str(book["_id"]),
        "title": book["title"],
        "author": book["author"]
    }
