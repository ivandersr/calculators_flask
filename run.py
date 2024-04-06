from src.main.server.server import app

if __name__ == "__main__":
    app.run(host="localhost", port=3333, debug=True)