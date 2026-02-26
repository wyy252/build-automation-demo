from flask import Flask, jsonify

def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/")
    def home():
        return "Build Automation Demo Successful!"

    @app.get("/health")
    def health():
        return jsonify(status="ok")

    def add(a: int, b: int) -> int:
        return a + b

    app.add = add  

    return app


if __name__ == "__main__":
    application = create_app()
    application.run(host="0.0.0.0", port=5000)