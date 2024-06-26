
from flask import Flask, render_template
from database import db
from config import Config
# from controllers.region_controller import region_bp
# from controllers.city_controller import city_bp
# from controllers.place_controller import place_bp
# from controllers.review_controller import review_bp

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


@app.route('/')
def index():
    # Replace with your logic to fetch the top 9 places with most reviews
    top_places = []  # Replace with actual logic
    return render_template('index.html', top_places=top_places)

# app.register_blueprint(region_bp)
# app.register_blueprint(city_bp)
# app.register_blueprint(place_bp)
# app.register_blueprint(review_bp)

if __name__ == '__main__':
    app.run(debug=True)
        