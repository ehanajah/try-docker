from quart import current_app

from app.main import create_app

app = create_app()

@app.route("/health")
async def health():
    await current_app.db.command("ping")

    return {
        "status": "ok"
    }

if __name__ == "__main__":
    app.run(debug=True)