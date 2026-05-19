from quart import Blueprint, request, jsonify, current_app
from app.services.book_service import *
from app.models.book import serialize_book

book_bp = Blueprint("books", __name__)

@book_bp.get("/")
async def get_books():
    books = await get_all_books(current_app.db)
    return jsonify([serialize_book(b) for b in books])

@book_bp.get("/<book_id>")
async def get_single_book(book_id):
    book = await get_book(current_app.db, book_id)
    return jsonify(serialize_book(book))

@book_bp.post("/")
async def create():
    data = await request.json
    book_id = await create_book(current_app.db, data)
    return jsonify({"id": book_id})

@book_bp.put("/<book_id>")
async def update(book_id):
    data = await request.json
    await update_book(current_app.db, book_id, data)
    return jsonify({"message": "updated"})

@book_bp.delete("/<book_id>")
async def delete(book_id):
    await delete_book(current_app.db, book_id)
    return jsonify({"message": "deleted"})
