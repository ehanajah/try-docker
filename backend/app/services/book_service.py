from bson import ObjectId

async def get_all_books(db):
    books = []
    async for book in db.books.find():
        books.append(book)
    return books

async def get_book(db, book_id):
    return await db.books.find_one({"_id": ObjectId(book_id)})

async def create_book(db, data):
    result = await db.books.insert_one(data)
    return str(result.inserted_id)

async def update_book(db, book_id, data):
    await db.books.update_one(
        {"_id": ObjectId(book_id)},
        {"$set": data}
    )

async def delete_book(db, book_id):
    await db.books.delete_one({"_id": ObjectId(book_id)})
    