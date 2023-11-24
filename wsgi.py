# wsgi.py
from app import app

if __name__ == "__main__":
    app.run()

host = os.environ.get("HOST", "0.0.0.0")
    port = os.environ.get("PORT", 5000)

    app.run(host=host, port=port)
