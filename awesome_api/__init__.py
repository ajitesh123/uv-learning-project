from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return {"message": "Welcome to Awesome API!"}

    return app
