"""Example of module Flask"""
from flask import Flask, render_template
from examples.modules_examples.flask_and_dash_example.dashboard import dashboard_emotions


def create_app():
    """Crates an APP"""
    app = Flask(__name__, instance_relative_config=False)

    @app.route("/")
    def index():
        return render_template("index.html")

    tweet = "It was one of the best years of my life! Although there were difficulties sometimes."
    app = dashboard_emotions(app, tweet)
    return app


if __name__ == '__main__':
    APP = create_app()
    APP.run(port=3748)
