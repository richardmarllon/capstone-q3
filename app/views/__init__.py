from flask import Flask

def init_app(app: Flask):
    from app.views.user_locator_view import bp as bp_locator

    app.register_blueprint(bp_locator)
