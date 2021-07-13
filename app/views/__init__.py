from flask import Flask

def init_app(app: Flask):
    from app.views.user_locator_view import bp as bp_locator
    from app.views.car_view import bp as bp_car
    from app.views.user_lesse_view import bp as bp_lesse
    from app.views.record_lesse_view import bp as bp_rec_lesse

    app.register_blueprint(bp_locator)
    app.register_blueprint(bp_rec_lesse)
    app.register_blueprint(bp_car)
    app.register_blueprint(bp_lesse)

