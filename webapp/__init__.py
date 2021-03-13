from flask import Flask, render_template
from webapp import database


def create_app():
    app = Flask(__name__)
    db = database.DB()

    @app.route("/")
    def index():
        title = "SeoFork"
        data = db.get_from_date_report("2021-01-19", "lenta.com")
        return render_template("dashboard/index.html", page_title=title, data=data)

    @app.route("/semantic")
    def semantic():
        title = "Семантика"
        data = db.get_from_date_report("2021-01-19", "lenta.com")
        return render_template("dashboard/index.html", page_title=title, data=data)

    return app
