from quart import Quart
from motor.motor_asyncio import AsyncIOMotorClient
from app.config import Config

def create_app():
    app = Quart(__name__)

    app.mongo_client = AsyncIOMotorClient(Config.MONGO_URI)
    app.db = app.mongo_client[Config.DB_NAME]

    from app.routes.book_routes import book_bp
    app.register_blueprint(book_bp, url_prefix="/api/books")

    return app
